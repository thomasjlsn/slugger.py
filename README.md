# slugger.py

Convert strings to slugs => convert-strings-slugs

---

## Usage

By default, `slugger.py` will convert a given string of words into a URL
slug, using hyphens (`-`) as a delimiter. The result is copied to the
system clipboard.

**Basic:**
```
python3 slugger.py
```

## Arguments

`slugger.py` may also be run with optional command line arguments that will
modify it's default behavior.

**-d C --delimiter C**

use char `C` instead of the defalt delimiter.

**-r --raw**

print results to standard out, then quit (useful for automating/scripting
slugger).

**-s --skip**

do not remove pullwords from the string.

**Example:**
*Use underscore instead of hyphen as delimiter*
```
python3 slugger.py -d _
```

---

## Configuration

slugger.py is configured with the files pullwords.txt and exceptions.txt,
containing newline delimited words to remove from the slug, and words to
preserve, respectively. These files need to live in the same directory as
slugger.py. If they do not exist they can be created with:

**Linux:**
```
touch exceptions.txt
touch pullwords.txt
```

**Windows:**
```
type nul > exceptions.txt
type nul > pullwords.txt
```

---

## Installation

**quick download:**
*you can download just the script with the following:*
```
curl -o slugger.py https://raw.githubusercontent.com/thomasjlsn/slugger.py/master/slugger.py
```

