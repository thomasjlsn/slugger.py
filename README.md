# slugger.py

slugger('slugger.py converts strings to slugs') ->  slugger-py-converts-strings-slugs

---

## Usage

```
python3 slugger.py
```

By default, `slugger.py` will convert a given string of words into a URL
slug, using hyphens (`-`) as a delimiter. The result is copied to the
system clipboard.

## Arguments

`slugger.py` may also be run with optional command line arguments that will
modify it's default behavior.

**-d C --delimiter C**

*defult: -*

Use char `C` instead of the defalt delimiter.

**-i STRING --input STRING**

convert `STRING` to a URL slug, then quit. **note**: `STRING` must be quoted
if it contains whitespace.

**-m N --minlen N**

*default: 3*

Set minimum length `N` of words to keep in the slug.

**-r --raw**

Suppress `Copied "..." to clipboard` message. If used in conjunction with
the `-i` argument, results are printed to standard out instead of copying
to clipboard.

**-s --skip**

Do not remove pullwords from the string. This argument overrides `-m`.

**-u --url-encode**

Percent encode special characters instead of removing them

**Example:**

**-** *Use underscore instead of hyphen as delimiter*
```
python3 slugger.py -d _
```

---

## Configuration

slugger.py is configured with the files pullwords.txt and exceptions.txt,
containing newline delimited words to remove from the slug, and words to
preserve, respectively. These files need to live in the same directory as
slugger.py. If they do not exist they can be created with:

**Linux / Mac:**
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

**via git:**
```
git clone https://github.com/thomasjlsn/slugger.py
```

**[download the script here](https://raw.githubusercontent.com/thomasjlsn/slugger.py/master/slugger.py)**
*or run the command:*
```
curl -o slugger.py https://raw.githubusercontent.com/thomasjlsn/slugger.py/master/slugger.py
```

**[download the zip here](https://github.com/thomasjlsn/slugger.py/archive/master.zip)**
*or run the command:*
```
curl -o slugger.zip https://github.com/thomasjlsn/slugger.py/archive/master.zip
```
