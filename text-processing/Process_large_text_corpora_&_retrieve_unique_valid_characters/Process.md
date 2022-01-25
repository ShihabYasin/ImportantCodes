

### Process large text corpora & retrieve unique valid characters:
1. Split text in small_text_data files
```shell
split --lines=999999 --numeric-suffixes --suffix-length=3 large_text.txt small_text-
```
2. Check for unicode character correction
3. Generate vocab.json for all small text files
4. Merge keys from all small text vocab.json in a set.
5. If successful it will generate ```all_vocab_keys.txt``` file.