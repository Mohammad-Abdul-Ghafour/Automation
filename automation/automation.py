import re


def get_emails_phones():

    with open('automation/assets/potential-contacts.txt','r') as f:
        file = f.read()
    regex = r'([\w.+-]+@[\w-]+\.[\w.-]+)'
    emails = re.findall(regex,file)   
    emails.sort()

    with open('automation/assets/emails.txt','w') as f:
        arr =[]
        for i in emails:
            if i not in arr:
                f.write(i+'\n')
            arr.append(i)

    regex = r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'
    phones = re.findall(regex,file)
    for j,i in enumerate(phones):
        if '(' in i:
            i = i.replace('(','')
            i = i.replace(')','-')
        if '.' in i:
            i = i.replace('.','-')
        if len(i) == 10:
            x=""
            for jj,val in enumerate(i):
                x += i[jj]
                if jj == 2 :
                    x += "-"
                if jj == 6:
                    x+="-"
            i = x
        phones[j]=i
    phones.sort()    

    with open('automation/assets/phone_numbers.txt','w') as f:
        arr =[]
        for i in phones:
            if i not in arr:
                if len(i) > 10:
                    f.write(str(i)+'\n')
                else:
                    f.write('206-'+ str(i)+'\n')
            arr.append(i)

get_emails_phones()