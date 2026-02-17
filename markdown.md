
# Python Code Learned

This is a list of Python code and concepts I have learned so far. 

The purpose of this list is to practice and retain the information. 

___

## Variables
String  
`name = '`Andrea L. MacGown`'`

Number  
`my_age =` 29

### Changing case  
`name = ` `'`Andrea L. MacGown`'`
`print(name.lower())`  
andrea l. macgown  

`print(name.upper())`  
ANDREA L. MACGOWN

### Adding Whitespace  

#### Tab  
`print('\t')`  

#### New Line  
`print('\n')`

### Stripping Whitespace  
 
`name.rstrip()`    
`name.lstrip()`  
`name.strip()`

## Numbers
`+` addition  
`-` subtraction  
`/` division  
`*` multiplication  
`//` floor division  

    20 // 6 = 3
    7 // 3 = 2
`%` modulo  

    5 % 3 = 2
    14 % 9 = 5    
`**` exponent  
    
    3 ** 3 = 27 

## Lists 

### Adding elements to a list

`.append()` 

    roman.dictators = ['Caesar', 'Pompey', 'Crassus']
    roman_dictators.append('Octavian')


### Deleting from a position
`del `  

    del roman_dictators[0]

### Remove by value

    roman_dictators.remove('Caesar')

### Other

Length of the list  
`len(`list`)`

Print in reverse order  
colors`.reverse()`

Permanent alphabetical sort  
colors`.sort()`

Temporary alphabetical sort  
colors`.sorted()`

Permanent reversing a list  
colors`.reverse()`


## Loops

### Range  

    for value in range(1,4):
        print(value)
1  
2  
3  

### List of numbers  
`list(range(1,4))`  
[1, 2, 3]

## If Statements

### Checking if a value is not in a list

`colors = ['`blue`', '`pink`', '`orange`']`

`forest = '`green`'`

`if forest not in colors:`  
`print(forest.title())`  
Green

### Checking if a list is not empty
    nyc = []
    if nyc:
        for area in nyc:
            print('These are the areas I have been to in New York)
    else:
        print('I have not visited New York City.')