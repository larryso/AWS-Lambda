from log.logger import logger

my_logger = logger()

my_list = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']

my_logger.info(my_list[0])
my_list.append("Geeks2")

for i in my_list:
    my_logger.info(i)





