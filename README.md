# slugger.py

slugger('slugger.py converts strings to slugs') ->  slugger-py-converts-strings-slugs

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

*defult: -*

Use char `C` instead of the defalt delimiter.

**-m N --minlen N**

*default: 3*

Set minimum length `N` of words to keep in the slug.

**-r --raw**

Print results to standard out, then quit (useful for automating/scripting
slugger).

**-s --skip**

Do not remove pullwords from the string. This argument overrides `-m`.

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
