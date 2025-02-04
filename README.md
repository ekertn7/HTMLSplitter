# Script to split original html into fixed length fragments

[Task statement](/src/statement.pdf)

## Project structure

```
.
├── README.md
├── app
│   ├── argument_parser
│   │   └── argument_parser.py  # cli arguments parser
│   ├── exceptions
│   │   └── exceptions.py       # exceptions
│   └── html_splitter
│       └── html_splitter.py    # script
├── config.py                   # config
├── pyproject.toml              # poetry requirements
├── pytest.ini                  # pytest config
├── split_msg.py                # entry point
└── tests
    └── test_split_message.py   # tests
```

## Downloading

```
git clone git@github.com:ekertn7/HTMLSplitter.git
cd HTMLSplitter
```

## Set up and launch

```
poetry install --with dev
poetry run python split_msg.py --max-len=1024 src/source.html
```

<details>
<summary>Example</summary><br>

```
poetry run python split_msg.py --max-len=512 src/minisource.html
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- fragment #1: 404 chars --
<div>
<span>
<a href="https://mockdata.atlassian.net/browse/ABC-12345"><code>ABC-12345</code></a> Ut finibus urna sed lorem elementum.
<a href="https://mockdata.atlassian.net/browse/ABC-12456"><code>ABC-12456</code></a> Eget tristique magna vulputate.
<a href="https://mockdata.atlassian.net/browse/ABC-12567"><code>ABC-12567</code></a> Sed a orci at turpis commodo semper quis vitae erat.
</span>
</div>
-- fragment #2: 480 chars --
<div>
<span>
<a href="https://mockdata.atlassian.net/browse/ABC-12678"><code>ABC-12678</code></a> Quis purus et augue varius egestas.
<a href="https://mockdata.atlassian.net/browse/ABC-12186"><code>ABC-12186</code></a> Faucibus dui.
<a href="https://mockdata.atlassian.net/browse/ABC-12384"><code>ABC-12384</code></a> In augue lacus, volutpat porta erat non…
<a href="https://mockdata.atlassian.net/browse/ABC-12406"><code>ABC-12406</code></a> Aliquet mattis felis.
</span>
</div>
-- fragment #3: 390 chars --
<div>
<span>
<a href="https://mockdata.atlassian.net/browse/ABC-12419"><code>ABC-12419</code></a> Nam non neque diam.
<a href="https://mockdata.atlassian.net/browse/ABC-12509"><code>ABC-12509</code></a> Donec sed sodales metus.
<a href="https://mockdata.atlassian.net/browse/ABC-12535"><code>ABC-12535</code></a> Aliquam sagittis bibendum tellus, sed feugiat lacus mattis eu.
</span>
</div>
```

</details>

## Bonus (can be launched with shebang)

```
echo "#\!$(poetry env info --path)/bin/python\n$(cat split_msg.py)" > split_msg.py
./split_msg.py --max-len=1024 src/source.html
```

## Launch tests

```
poetry run pytest -v
```
