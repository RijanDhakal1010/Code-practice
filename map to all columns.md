How can I map multiple columns of a pandas data-frame to a dict at the same time?

Details below:

Say, I table that looks as follows:

| Index  | one | two |
| ------ | --- | --- |
| first  | A   | B   |
| second | C   | D   |

I have a dict {A:'Apple', B:'Ball', C:'Cat',D:'Dog'}

Desired output is a new data-frame where the cells of multiple selected columns are mapped to and replaced with the values of a supplied dict:

| Index  | one   | two  |
| ------ | ----- | ---- |
| first  | Apple | Ball |
| second | Cat   | Dog  |

Ideally want to keep the Index column.

I can use `dataframe['one column'].map(dict)` to map one column at a time but on a large data-frame with many columns doing this manually would be difficult. But seems multiple columns are not allowed:

```python
df.iloc[:,1:].map(dict)
```

Produces the error : `'DataFrame' object has no attribute 'map'`

I tried using `apply()`  with `lambda` and `replace()`as follows

```python
df.iloc[:,1:].apply(lambda x: x.replace(dict[x]))
# using .iloc[:,1:] to try and keep the index
```

Turns out dicts cannot be used in this way.

A  MacGyvered solution that I am using right now is:

```python
df2 = pd.DataFrame()
df2['Index'] = df1['Index']
for i in df1.columns[1:]:
    df2[i] = df1[i].map(dict)
```

Gets the job done, but is there anything better within pandas I should be aware of?
