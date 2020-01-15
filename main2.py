from DBcm import UseDatabase
from settings import DATABASE_CONFIG

def main():
    with UseDatabase(DATABASE_CONFIG) as cursor:
        sql = 'select * from first_name'
        cursor.execute(sql)
        # w pytonie 3.8 mamy:
        # while row := cursor.fetchone():
        #     print(row)

        row = cursor.fetchone()
        print(row)
        while row:
            row = cursor.fetchone()
            print(row)


if __name__ == '__main__':
    main()