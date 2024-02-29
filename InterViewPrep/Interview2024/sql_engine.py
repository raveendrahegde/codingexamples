# Q: Read ./sql.md

import re

class SQL():
  def __init__(self, parser) -> None:
    self.library = [
      {
          'title': 'The Ministry for the Future',
          'author': 'Kim Stanley Robinson',
          'year': 2020,
      },
      {
          'title': 'Circe',
          'author': 'Madeline Miller',
          'year': 2018,
      },
      {
          'title': 'Song of Achilles',
          'author': 'Madeline Miller',
          'year': 2012,
      },
      {
          'title': 'Designing Climate Solutions',
          'author': 'Hal Harvey',
          'year': 2018,
      },
    ]

    self.parser = parser
  
  def getQuery(self):
    query = input("Enter query:")
    return query

  def runQuery(self, query):
    result = []
    match = self.parser.match(query)
    WHERE = match.group(2)

    for item in self.library:
      all_conditions = []
      selected = True
      
      if WHERE:
        conditions = [condition.strip() for condition in WHERE.split('AND')]
        for condition in conditions:
          pattern = re.compile(r"(\w+)\s*([><=]+)\s*'?([^']+)'?") # Pattern inside WHERE clause
          (key, symbol, val) = pattern.match(condition).groups()

          all_conditions.append({'key': key, 'symbol': symbol, 'val': val})
      
      for condition in all_conditions:
        if condition['symbol'] == '=':
          if item[condition['key']] != condition['val']:
            selected = False
            break
        elif condition['symbol'] == '>':
          if item[condition['key']] <= int(condition['val']):
            selected = False
            break

      if selected:
        result.append(item)

    return result

  def printResult(self, result):
    if result:
      SELECT, WHERE, ORDERBY = self.parser.match(query).groups()
      fields= SELECT.split(',')
      
      if ORDERBY:
        sorted(result, key=lambda item: item['year'])

      title = '|'.join([field + " " * len(str(result[0][field.strip()])) for field in fields])
      lines = "-" * len(title)

      print(f"{title}\n{lines}")

      for item in result:
        line = ''
        print("  |  ".join([str(item[field.strip()]) for field in fields]))

if __name__ == "__main__":
  PARSER = re.compile(r'^SELECT (.*) FROM [a-z]+(?: WHERE (.*?))?(?: ORDER BY (.*?))?$')
  sql = SQL(PARSER)
  
  while True:
    query = sql.getQuery()
    # query = "SELECT title, author FROM library WHERE author = 'Madeline Miller'"
    result = sql.runQuery(query)
    sql.printResult(result)
