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
import subprocess
import time
import requests
import os

def get_mizar_env():
    """Get the environment variables required for Mizar to run."""
    env = os.environ.copy()
    env['MIZFILES'] = '/usr/local/share/mizar'
    return env

def test_verify_py_integration():
    """
    Integration test for verify.py.
    Runs the script on the sample Mizar file and checks the output.
    """
    filename = "tests/test.miz"
    env = get_mizar_env()
    result = subprocess.run(
        ['python', 'verify.py', filename],
        capture_output=True,
        text=True,
        env=env
    )

    # A successful run should have a return code of 0 and no "Error" or "****" in the output.
    assert result.returncode == 0
    assert "Error" not in result.stdout
    assert "Error" not in result.stderr
    assert "****" not in result.stdout
    assert "****" not in result.stderr

def test_server_py_integration():
    """
    Integration test for the Flask server.
    Starts the server, sends a request to /verify, and checks the response.
    """
    # Start the server in a background process
    env = get_mizar_env()
    server_process = subprocess.Popen(['python', 'src/main.py'], env=env)

    # Give the server a moment to start up
    time.sleep(2)

    try:
        # Read the sample Mizar file
        with open("tests/test.miz", 'r') as f:
            mizar_code = f.read()

        # Send a request to the /verify endpoint
        response = requests.post("http://localhost:8080/verify", json={'code': mizar_code})

        assert response.status_code == 200
        json_data = response.json()
        # A successful run should not contain "Error" or "****" in the result.
        assert "Error" not in json_data['result']
        assert "****" not in json_data['result']

    finally:
        # Stop the server
        server_process.terminate()
        server_process.wait()
