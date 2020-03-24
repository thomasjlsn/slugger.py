# slugger.py

A python script to turn a string (in this case, a blog post title) into a URL slug.

Run with no arguments, `python3 slugger.py` will copy the output to the
system clipboard.
Given the `-r` or `--raw` flags, the output will be printed to standard out.

**quick download:**
```
curl -o slugger.py https://raw.githubusercontent.com/thomasjlsn/slugger.py/master/slugger.py
```

## Configuration

slugger.py is configured with the files pullwords.txt and exceptions.txt,
containing newline delimited words to remove from the slug, and words to
preserve, respectively. These files need to live in the same directory as
slugger.py. If they do not exist they can be created with:

**Linux**
```
touch exceptions.txt
touch pullwords.txt
```

**Windows**
```
type nul > exceptions.txt
type nul > pullwords.txt
```
