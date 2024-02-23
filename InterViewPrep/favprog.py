class ABCD:
    def __init__(self):
        self.__componentPath = []
        self.__topPath = []
        self.__depth=0

    def getComponentListfromTree(self, tree):
        self.__depth +=1
        try:
            for subtree in tree:
                compSignature=subtree['name'] + "|" + subtree['version']
                self.__componentPath.append(compSignature)
                _z=list(self.__componentPath)
                self.__topPath.append(_z)
                if 'subcomponents' in subtree and subtree['subcomponents']:
                    self.getComponentListfromTree(subtree['subcomponents']) 
                else:
                    self.__componentPath = self.__componentPath[:self.__depth-1]
                    pass
            self.__depth -= 1
            self.__componentPath = self.__componentPath[:self.__depth-1]
            return self.__topPath
        except Exception as e:
            print (str(e))


if __name__ == '__main__':
    tree=[{'name':'N1', 'version':'V1','subcomponents':
            [{'name':'N2', 'version':'V2','subcomponents':
               [{'name':'N3', 'version':'V3','subcomponents':[]}, {'name':'N4', 'version':'V4','subcomponents':[{'name':'N5', 'version':'V5','subcomponents':[]}]}]
            }]
        }]

    abcd=ABCD()
    ans=abcd.getComponentListfromTree(tree)
    for a in ans:
        print a