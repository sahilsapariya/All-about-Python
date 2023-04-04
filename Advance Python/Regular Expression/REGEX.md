# Regular Expressions in Python

[Reference](https://www.w3schools.com/python/python_regex.asp)

A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern.

## RegEx module
```bash 
import re
```

## RegEx functions

Function    |   Description
---|---
findall     |   Returns a list containing all matches
search      |   	Returns a Match object if there is a match anywhere in the string
split       |   Returns a list where the string has been split at each match
sub         |   Replaces one or many matches with a string
finditer    |   The finditer yields an iterator as a resultant with all the objects that match the one we sent it finditer supports more attributes than any other function defined above. It also provides more details related to the matched object

## Metacharacters

Metacharacters are characters with special meaning.
<!-- 
Character   |   Description |   Example
--- |   --- |   ---
[ ]  | set of characters  | "[a-z]"
\   | 	Signals a special sequence (can also be used to escape special characters)  | "\d"
.   |   Any character (except newline character)    | "he..o"
^   | Starts with | "^hello"
$   | Ends with | "planet$"
\*   | Zero or more occurrences |  -->


<table class="ws-table-all notranslate">
<tbody><tr>
<th style="width:120px">Character</th>
<th>Description</th>
<th style="width:120px">Example</th>
<!-- <th style="width:75px">Try it</th> -->
</tr>
<tr>
<td>[]</td>
<td>A set of characters</td>
<td>"[a-m]"</td>
<!-- <td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_regex_meta1">Try it »</a></td> -->
</tr>
<tr>
<td>\</td>
<td>Signals a special sequence (can also be used to escape special characters)</td>
<td>"\d"</td>
<!-- <td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_regex_meta2">Try it »</a></td> -->
</tr>
<tr>
<td>.</td>
<td>Any character (except newline character)</td>
<td>"he..o"</td>
<!-- <td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_regex_meta3">Try it »</a></td> -->
</tr>
<tr>
<td>^</td>
<td>Starts with</td>
<td>"^hello"</td>
<!-- <td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_regex_meta4">Try it »</a></td> -->
</tr>
  <tr>
<td>$</td>
<td>Ends with</td>
<td>"planet$"</td>
<!-- <td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_regex_meta5">Try it »</a></td> -->
  </tr>
  <tr>
<td>*</td>
<td>Zero or more occurrences</td>
<td>"he.*o"</td>
<!-- <td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_regex_meta6">Try it »</a></td> -->
  </tr>
  <tr>
<td>+</td>
<td>One or more occurrences</td>
<td>"he.+o"</td>
<!-- <td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_regex_meta7">Try it »</a></td> -->
  </tr>
  <tr>
<td>?</td>
<td>Zero or one occurrences</td>
<td>"he.?o"</td>
<!-- <td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_regex_meta10">Try it »</a></td> -->
  </tr>
  <tr>
<td>{}</td>
<td>Exactly the specified number of occurrences</td>
<td>"he.{2}o"</td>
<!-- <td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypythonasp?filename=demo_regex_meta8">Try it »</a></td> -->
  </tr>
  <tr>
<td>|</td>
<td>Either or</td>
<td>"falls|stays"</td>
<!-- <td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_regex_meta9">Try it »</a></td> -->
  </tr>
  <tr>
<td>()</td>
<td>Capture and group</td>
<td>&nbsp;</td>
<!-- <td>&nbsp;</td> -->
  </tr>
</tbody></table>



## Special Sequences


A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

<table class="ws-table-all notranslate">
<tbody><tr>
<th style="width:120px">Character</th>
<th>Description</th>
<th style="width:120px">Example</th>
<!-- <th style="width:75px">Try it</th> -->
</tr>
<tr>
<td>\A</td>
<td>Returns a match if the specified characters are at the beginning of the 
string</td>
<td>"\AThe"</td>
<!-- <td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_regex_seq1">Try it »</a></td> -->
</tr>
  <tr>
<td>\b</td>
<td>Returns a match where the specified characters are at the beginning or at the 
end of a word<br>(the "r" in the beginning is making sure that the string is 
being treated as a "raw string")</td>
<td>r"\bain"<br>r"ain\b"</td>
<!-- <td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_regex_seq2">Try it »</a><br> -->
<!-- <a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_regex_seq2-2">Try it »</a></td> -->
  </tr>
  <tr>
<td>\B</td>
<td>Returns a match where the specified characters are present, but NOT at the beginning 
(or at 
the end) of a word<br>(the "r" in the beginning is making sure that the string 
is being treated as a "raw string")</td>
<td>r"\Bain"<br>r"ain\B"</td>
<!-- <td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_regex_seq3">Try it »</a><br> -->
<!-- <a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_regex_seq3-2">Try it »</a></td> -->
  </tr>
  <tr>
<td>\d</td>
<td>Returns a match where the string contains digits (numbers from 0-9)</td>
<td>"\d"</td>
<!-- <td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_regex_seq4">Try it »</a></td> -->
  </tr>
  <tr>
<td>\D</td>
<td>Returns a match where the string DOES NOT contain digits</td>
<td>"\D"</td>
<!-- <td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_regex_seq5">Try it »</a></td> -->
  </tr>
  <tr>
<td>\s</td>
<td>Returns a match where the string contains a white space character</td>
<td>"\s"</td>
<!-- <td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_regex_seq6">Try it »</a></td> -->
  </tr>
  <tr>
<td>\S</td>
<td>Returns a match where the string DOES NOT contain a white space character</td>
<td>"\S"</td>
<!-- <td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_regex_seq7">Try it »</a></td> -->
  </tr>
  <tr>
<td>\w</td>
<td>Returns a match where the string contains any word characters (characters from 
a to Z, digits from 0-9, and the underscore _ character)</td>
<td>"\w"</td>
<!-- <td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_regex_seq8">Try it »</a></td> -->
  </tr>
  <tr>
<td>\W</td>
<td>Returns a match where the string DOES NOT contain any word characters</td>
<td>"\W"</td>
<!-- <td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_regex_seq9">Try it »</a></td> -->
  </tr>
<tr>
<td>\Z</td>
<td>Returns a match if the specified characters are at the end of the string</td>
<td>"Spain\Z"</td>
<!-- <td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_regex_seq10">Try it »</a></td> -->
</tr>
</tbody></table>

## Sets

A set is a set of characters inside a pair of square brackets [ ] with a special meaning:

<table class="ws-table-all notranslate">
<tbody><tr>
<th style="width:120px">Set</th>
<th>Description</th>
<!-- <th style="width:75px">Try it</th> -->
</tr>
  <tr>
<td>[arn]</td>
<td>Returns a match where one of the specified characters (<code class="w3-codespan">a</code>,
<code class="w3-codespan">r</code>, or <code class="w3-codespan">n</code>) is 
present</td>
<!-- <td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_regex_set1">Try it »</a></td> -->
  </tr>
  <tr>
<td>[a-n]</td>
<td>Returns a match for any lower case character, alphabetically between
<code class="w3-codespan">a</code> and <code class="w3-codespan">n</code></td>
<!-- <td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_regex_set2">Try it »</a></td> -->
  </tr>
  <tr>
<td>[^arn]</td>
<td>Returns a match for any character EXCEPT <code class="w3-codespan">a</code>,
<code class="w3-codespan">r</code>, and <code class="w3-codespan">n</code></td>
<!-- <td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_regex_set3">Try it »</a></td> -->
  </tr>
  <tr>
<td>[0123]</td>
<td>Returns a match where any of the specified digits (<code class="w3-codespan">0</code>,
<code class="w3-codespan">1</code>, <code class="w3-codespan">2</code>, or <code class="w3-codespan">
3</code>) are 
present</td>
<!-- <td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_regex_set4">Try it »</a></td> -->
  </tr>
  <tr>
<td>[0-9]</td>
<td>Returns a match for any digit between
<code class="w3-codespan">0</code> and <code class="w3-codespan">9</code></td>
<!-- <td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_regex_set5">Try it »</a></td> -->
  </tr>
<tr>
<td>[0-5][0-9]</td>
<td>Returns a match for any two-digit numbers from <code class="w3-codespan">00</code> and <code class="w3-codespan">
59</code></td>
<!-- <td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_regex_set6">Try it »</a></td> -->
</tr>
  <tr>
<td>[a-zA-Z]</td>
<td>Returns a match for any character alphabetically between
<code class="w3-codespan">a</code> and <code class="w3-codespan">z</code>, lower case OR upper case</td>
<!-- <td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_regex_set7">Try it »</a></td> -->
  </tr>
  <tr>
<td>[+]</td>
<td>In sets, <code class="w3-codespan">+</code>, <code class="w3-codespan">*</code>,
<code class="w3-codespan">.</code>, <code class="w3-codespan">|</code>,
<code class="w3-codespan">()</code>, <code class="w3-codespan">$</code>,<code class="w3-codespan">{}</code> 
has no special meaning, so <code class="w3-codespan">[+]</code> means: return a match for any
<code class="w3-codespan">+</code> character in the string</td>
<!-- <td><a target="_blank" class="w3-btn btnsmall btnsmall" href="trypython.asp?filename=demo_regex_set8">Try it »</a></td> -->
  </tr>
</tbody></table>


# Examples with code snipates

see the main.py file.