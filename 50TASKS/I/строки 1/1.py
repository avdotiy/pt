def search_substr(subst,st):
    subst = subst.lower()
    st = st.lower()
    if subst in st:
        return ('Есть контакт')
    else:
        return ('Мимо')
print (search_substr('matt', 'krutoy'))