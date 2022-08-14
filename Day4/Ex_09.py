# emails = ['test.email+alex@leetcode.com','test.e.mail+bob.cathy@leetcode.com', 'testemail+david@lee.tcode.com']
emails = ["fg.r.u.uzj+o.pw@kziczvh.com","r.cyo.g+d.h+b.ja@tgsg.z.com","fg.r.u.uzj+o.f.d@kziczvh.com","r.cyo.g+ng.r.iq@tgsg.z.com","fg.r.u.uzj+lp.k@kziczvh.com","r.cyo.g+n.h.e+n.g@tgsg.z.com","fg.r.u.uzj+k+p.j@kziczvh.com","fg.r.u.uzj+w.y+b@kziczvh.com","r.cyo.g+x+d.c+f.t@tgsg.z.com","r.cyo.g+x+t.y.l.i@tgsg.z.com","r.cyo.g+brxxi@tgsg.z.com","r.cyo.g+z+dr.k.u@tgsg.z.com","r.cyo.g+d+l.c.n+g@tgsg.z.com","fg.r.u.uzj+vq.o@kziczvh.com","fg.r.u.uzj+uzq@kziczvh.com","fg.r.u.uzj+mvz@kziczvh.com","fg.r.u.uzj+taj@kziczvh.com","fg.r.u.uzj+fek@kziczvh.com"]
lst = []
new_lst = []
for email in emails:
    lst.append(email.split("@"))
print(lst)
for i in lst:
    i[0] = i[0].replace('.', '')
    print(i[0])
    i[0] = i[0].split("+")[0]
    if i not in new_lst:
        new_lst.append(i)
print(lst)
print(new_lst)
if lst == new_lst:
    print(len(lst))
else:
    print(len(new_lst))


