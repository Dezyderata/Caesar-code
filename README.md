Caesar is a Python module encoding and decoding Caesar code.

#### Instalation:

- Download .whl package from [release page](https://github.com/Dezyderata/Caesar-code/releases/tag/v1.0).
- Install using pip

#### Runing:

- caesar_cli - runs CLI application,
- caesar_web - runs web application.

##### CLI application:
	 
	usage: usage: caesar_cli [-h] --offset OFFSET --text TEXT {encrypt,decrypt}

	positional arguments:
	  {encrypt,decrypt}  Possible actions

	optional arguments:
	  -h, --help         show this help message and exit
	  --offset OFFSET    Shift by number. Argument is required.
	  --text TEXT        Text to shift. Argument is required.

###### Example runs:
	
	$ caesar_cli encrypt --offset 7 --text 'Ala ma kota'
	Hsh th rvah
	
	$ caesar_web
	 * Serving Flask app "caesar_web" (lazy loading)
         * Environment: production
           WARNING: This is a development server. Do not use it in a production deployment.
           Use a production WSGI server instead.
         * Debug mode: off
         * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
	# Run in another console
	$ curl http://localhost:5000/encrypt/7/AlaMaKota
        HshThRvah
