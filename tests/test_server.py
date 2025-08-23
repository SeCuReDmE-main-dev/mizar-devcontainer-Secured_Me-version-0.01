#
#
#
#                                 .....      ...
#                           ...... .   .````.   .  . .. .
#                     ........... . .l~[[][_?+l` .      .....
#                  ............... :[_<<,!i'I{[]I .     .........
#               ................. ^1i-'>>][<~^[-{, .    ...........
#             ................... <-I^`/?\\?/^.i~_ .    ..............
#           ..................... "1I!'+<}{~_`l;{: .    ...............
#          .'..................... l]~I,:l!,;:<]! .     .......  ........
#        .'........................ `>~]]?-?}+>^ .      ..  ..   ....... .
#       .'..........................  .'^",^'.  ..    .   ..    ........  .
#      .'''''.................   . .                     ..    ......... . ..
#     .'''''.`'''''''''''...'.<]+>_i[+]__+}~[<,]]-+-_-`...    .......... .  .
#     '''''''   .        ...  lI!;l:!l: ^^l,;"`l^l,'::                  . .  .
#    .''''''./f(i-tr?~j|{.''[u':   ^. ~x)>+/r|"iul x{\_|nf]t!<|+j()ln|]. ... .
#    ''''''` oZf<>[qfravk..,oxU[O_O): /Znx^\B,"odh"$vM|"Wn^B?1hn#ud]qrz^ . . .
#    '''''''.QJj~\dz?/Zf0^.)Q;Z}cju '.-tXO _q |Z-d|O{mi O1 XcXj\Q; itxp, .  . .
#   .''''''''`^,`^^", `"  :ji ';    . .,`     `   '   ^ .   "^      ",  .  .. .
#    ''''''''.,::!`';l:::::,":."I;:I^`;,^;;": ^;:^`:I: ,:;,,"::Il!;I:'..  .  .
#    ''''''''',;:!^;i><<:l~<i!.I<i<<,Ill<><ll"'>i!i:li`"i>i!>>ii;;:;,' . ..  .
#    .''''''''"^^`^+>Ill"I~i>>::~i>iI!`^l!l!;i`;:!i.I!I !!>il;Il`'''``.. .   .
#     '''''''^i><<>ii<i.i<l><>i>!il!!.I<~!lI>>i!"';ii!;.!:ii :l>!!!;;i` .   .
#     ''''''''.........'... . ,<~~^">~+;`i!<ii l!,i<,.   .  .          . .
#      ''''''''''''''''''''''''''`'``^^^``^`'....'.''...................   .
#       '`'''''''''''''''''.''..'`^^^^^^^^`'.......  ...................  .
#        '''''''''''''''''''''`^^^"""^^^^`'''''''....................... .
#         .`''''''''''''''''`^^^^^^^^^^`....... .........    ............
#           '`''''''''''''``'^I!!+++:^~!><: !'.iIl;^:.   ..............
#            .''''''''''`^^;-l--?,,-~~><;!~!+i>i+i+<l_~<I....
#              ..'''''`^""`_Y{unzi>nnz[c?]1j}{xxX1|(xc}r(
#               .````^""""""":,"^""'.'..^'.' . `''..'
#             .`^^,"""",,,,""^^^^`..'.......''```'.....
#         . .'^",,""",,,,,,,"^^^`''''.......`^```.....
#       .'''^",,,,",,,,,,,,""^^`'''''```''''````....
# '''''``^",,,",,,,,,,,,,""""^^^`^^^^'.......              ..''.
# ....^",,,,,,,,,::::,,,"""^`'..'```.                     .`'..
# .'`",,,"`^"^^",,,:,,"""^^.                          ..''''..

import pytest
import os
from unittest.mock import patch, MagicMock
from src.server import app

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Test that the index route returns a 200 status code."""
    response = client.get('/')
    assert response.status_code == 200

@patch('src.server.subprocess.run')
def test_verify_route_success(mock_subprocess_run, client):
    """Test the /verify route with a successful verification."""
    # Mock the subprocess result
    mock_result = MagicMock()
    mock_result.stdout = "Verification successful."
    mock_result.stderr = ""
    mock_subprocess_run.return_value = mock_result

    mizar_code = "environ begin theorem T1: 1 = 1;"
    response = client.post('/verify', json={'code': mizar_code})

    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['result'] == "Verification successful."

    # Check that the temp file was created and then removed
    assert not os.path.exists("temp_proof.miz")

@patch('src.server.subprocess.run')
def test_verify_route_mizf_not_found(mock_subprocess_run, client):
    """Test the /verify route when the 'mizf' command is not found."""
    mock_subprocess_run.side_effect = FileNotFoundError

    mizar_code = "environ begin theorem T1: 1 = 1;"
    response = client.post('/verify', json={'code': mizar_code})

    assert response.status_code == 200
    json_data = response.get_json()
    assert "Error: 'mizf' command not found." in json_data['result']

    # Check that the temp file was cleaned up
    assert not os.path.exists("temp_proof.miz")

@patch('src.server.os.remove')
@patch('src.server.subprocess.run')
def test_verify_route_cleans_up_on_error(mock_subprocess_run, mock_os_remove, client):
    """Test that the temporary file is removed even if an error occurs."""
    mock_subprocess_run.side_effect = Exception("A random error")

    mizar_code = "environ begin theorem T1: 1 = 1;"
    response = client.post('/verify', json={'code': mizar_code})

    assert response.status_code == 200
    json_data = response.get_json()
    assert "An unexpected error occurred" in json_data['result']

    # Check that os.remove was called on the temp file
    mock_os_remove.assert_called_with("temp_proof.miz")
