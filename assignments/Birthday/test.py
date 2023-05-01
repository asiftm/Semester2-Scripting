date_formats = ['%Y-%m-%d',
                    '%Y/%m/%d',
                    '%m-%d-%Y',
                    '%m/%d/%Y',
                    '%d-%m-%Y',
                    '%d/%m/%Y',
                    '%Y-%m-%d',
                    '%m/%d/%Y',
                    '%d-%m-%Y',
                    '%d/%m/%Y',
                    '%Y-%m-%d',
                    '%m/%d/%Y',
                    '%d-%m-%Y',
                    '%d/%m/%Y',
                    '%Y-%m-%d',
                    '%m/%d/%Y',
                    '%d-%m-%Y',
                    '%d/%m/%Y'
                    ]
for i in date_formats:
    while date_formats.count(i)>1:
        date_formats.remove(i)

print(date_formats)