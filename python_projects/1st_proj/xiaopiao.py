print('.................................................')
order = input('请输入单号：')
wp1 = input('请输入商品名称：')
a = int(input('请输入商品数量：'))
b = float(input('请输入单价：'))
wp2 = input('请输入商品名称：')
c = int(input('请输入商品数量：'))
d = float(input('请输入单价：'))
wp3 = input('请输入商品名称：')
e = int(input('请输入商品数量：'))
f = float(input('请输入单价：'))
wp4 = input('请输入商品名称：')
i = int(input('请输入商品数量：'))
j = float(input('请输入单价：'))
zj1 = a * b
zj2 = c * d
zj3 = e * f
zj4 = i * j
print('时间：','2025-10-10 17;10:10')
print('单号：',order)
print('.................................................')
print('名称         ','数量  ','单价   ','金额   ')
print(wp1,a,' ',b,'  ',zj1)
print(wp2,c,' ',d,'  ',zj2)
print(wp3,e,' ',f,'  ',zj3)
print(wp4,i,' ',i,'  ',zj4)
print('.................................................')
number = a + c + e + i
ze = zj1 + zj2 + zj3 + zj4
print('总数：',number,'      ','总额：',round(ze,2))
print('折后总额：',round(ze,2))
print('实收：',round(ze,2),'找零：','0.00')
print('收银：管理员')
print('.................................................')