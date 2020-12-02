# Problem
Leonard, a researcher, has been tasked with sampling adjacent cities in twelve US states to see if COVID-19 is present within the population. Unfortunately, his employers have only given him a budget that allows him to visit each city once. Given the input, determine if Leonard can visit each city only once and return home in one trip.

### Notes:
* Leonard can start his trip from any of the cities that he's supposed to visit in a given state.
* He can only visit one city twice; the city of origin for his trip. (Allowed because Leonard needs to return home!)

## Explanation
The first given line is ***n*** and ***r***. 
* ***n***: Number of cities Leonard must travel to.
* ***r***: Number of paths between cities given.

For the next ***r*** lines, you are given the known paths between two cities.

Each path is delimited by an arrow: "->"

Return "Possible" if Leonard can visit each city only once and return home.

Return "Not Possible" if Leonard can not visit each city only once and return home.

## Sample Input/Ouput

### Sample Input 1
```
5 6
Orlando -> Largo
Key West -> Jacksonville
Clearwater -> Orlando
Jacksonville -> Miami
Largo -> Key West
Miami -> Clearwater
```

### Sample Output 1
`Possible`

### Sample Input 2
```
8 10
Atlanta -> Savannah
Atlanta -> Athens
Savannah -> Macon
Savannah -> Norcross 
Macon -> Athens
Macon -> Helen
Norcross -> Savannah
Norcross -> Griffin
Athens -> Douglasville
Douglasville -> Griffin
```

### Sample Output 2
`Not Possible`

## Inputs
All inputs are available in the `stdin` file.
