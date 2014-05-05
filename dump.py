#!/usr/bin/python

# Run with:
#   python hello.py cameron
#   python hello.py


# import modules used here -- sys is a very standard one
import sys
import subprocess
import getpass
import ConfigParser
import datetime
# from subprocess import Popen, PIPE, STDOUT

# Gather our code in a main() function
def main():

  # print 'Number of arguments: ', len(sys.argv)
  config = ConfigParser.ConfigParser()
  config.read('dump.cfg')

  for db in config.sections():
    if config.getboolean(db, 'active'):
      # print config.get(db)
      # os.mkdir()
      # mkdir -p "$MYSQLDUMP_HOST" && ssh $MYSQLDUMP_HOST "mysqldump -u'$MYSQLDUMP_USER' -p '$MYSQLDUMP_DB' | gzip -3 -c" > "$MYSQLDUMP_HOST/${MYSQLDUMP_DB}_`date +%Y%m%d_%H%M%S`.sql.gz"

  sys.exit(0)

  host = sys.argv[1]
  database = sys.argv[2]
  # while 1:
  #   try:
  #     line = sys.stdin.readline()
  #   except KeyboardInterrupt:
  #     break

  #   if not line:
  #     break
  #   # ssh aap-dev "mysqldump -uroot -p altech_autopage | gzip -3 -c" > altech_autopage_`date +%Y%m%d_%H%M%S`.sql.gz
  #   print line.strip()
  filename = database+"_"+datetime.datetime.now().strftime('%Y%m%d_%H%M%S')+".sql.gz"
  dumpfile = open(filename, 'w')
  # p = Popen(['grep', 'f'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
  # subprocess.call(['ls', '-l'], stdout=dumpfile)
  passs = getpass.getpass("Key password: ")
  p = subprocess.Popen(["ssh", host, "mysqldump -uroot -p "+database+" | gzip -3 -c"], stdin=subprocess.PIPE, stdout=dumpfile)
  # p.communicate(input=passs+'\ntwo\nthree\nfour\nfive\nsix\n')[0]
  # p.communicate(input=passs)[0]
  print passs
  p.stdin.write(passs+"\n")
  # subprocess.call(["ssh", "aap-dev", "mysqldump -uroot -p'"+passs+"' altech_autopage | gzip -3 -c"], stdout=dumpfile)


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()
