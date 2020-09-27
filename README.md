Caesar is a Python module encoding and decoding Caesar code.

Instalation:
	Download .whl package from https://github.com/Dezyderata/Caesar-code/releases/tag/v1.0.
	Install using pip

Runing:
	caesar_cli - runs CLI application,
	caesar_web - runs web application.

CLI application:
	 
	usage: usage: caesar_cli [-h] --offset OFFSET --text TEXT {encrypt,decrypt}

	positional arguments:
	  {encrypt,decrypt}  Possible actions

	optional arguments:
	  -h, --help         show this help message and exit
	  --offset OFFSET    Shift by number. Argument is required.
	  --text TEXT        Text to shift. Argument is required.

Web application shows listening port in CLI.

Example runs:
	
	caesar_cli encrypt --offset 7 --text 'Ala ma kota'
	
	http://127.0.0.1:5000/encrypt/7/Alamakota
	
	
	
	
