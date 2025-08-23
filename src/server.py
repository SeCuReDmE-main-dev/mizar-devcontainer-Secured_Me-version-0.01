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

import subprocess
import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    """Serves the main HTML page."""
    return render_template('index.html')

@app.route('/verify', methods=['POST'])
def verify():
    """Receives Mizar code, runs the verifier, and returns the result."""
    code = request.json.get('code', '')
    
    # Securely create a temporary file to store the proof
    proof_filename = "temp_proof.miz"
    with open(proof_filename, 'w') as f:
        f.write(code)

    # Run the Mizar verifier command in a subprocess
    try:
        result = subprocess.run(
            ['mizf', proof_filename],
            capture_output=True,
            text=True,
            timeout=30  # Add a timeout for safety
        )
        
        # Combine standard output and standard error for a full report
        output = result.stdout + result.stderr
        
    except FileNotFoundError:
        output = "Error: 'mizf' command not found. Are you running this inside the Mizar Dev Container?"
    except Exception as e:
        output = f"An unexpected error occurred: {e}"
    finally:
        # Clean up the temporary file
        if os.path.exists(proof_filename):
            os.remove(proof_filename)

    return jsonify({'result': output})
