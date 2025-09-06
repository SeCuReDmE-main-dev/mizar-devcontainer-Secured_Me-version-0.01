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

import sys
import subprocess

def run_verifier(filename):
    """Runs the Mizar verifier on a given file."""
    if not filename:
        print("Error: Please provide a filename.")
        print("Usage: python verify.py <your_proof.miz>")
        return

    print(f"Verifying {filename}...")
    try:
        result = subprocess.run(
            ['mizf', filename],
            capture_output=True,
            text=True
        )
        # Print the combined output
        print(result.stdout + result.stderr)
    except FileNotFoundError:
        print("Error: 'mizf' command not found. Are you running this inside the Mizar Dev Container?")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Get filename from command line arguments
    file_to_check = sys.argv[1] if len(sys.argv) > 1 else None
    run_verifier(file_to_check)
