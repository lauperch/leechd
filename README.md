# leechd - find your stolen stuff

## Install
``` # git clone https://github.com/lauperch/leechd.git ```

## Use
### just run it
First, adjust the parameters for your searchObject in the entry pint. Then:    
``` # python leechd.py ```
### implement in other class
``` python
searchObject = SearchObject(term, areacode, radius)
leechd       = Leechd(searchObject)
leechd.start()
...
leechd.stop()
```
## Contribute
``` 
# git checkout -b new_feature
...
# git commit -am "added new_feature"
# git push origin new_feature
```
## TODO
* add more sites to search on
* add nicer UI
