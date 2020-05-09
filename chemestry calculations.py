version = 0

if version == 0:
    print('1: calculates the percentage of each element in a substance.')
    print('2: calculates N, n, M, and m.')
    print('3: calculates impirical and molecular formulas.')
    print('4: calculates percentage of elements.')
    print('5: calculates ratios (2H2 + O2 = 2H2O).')
    print('6: calculates average atomic mass.')
    print('7: calculates the percent of two isotopes of an average atomic mass.')
    version = int(input('which mode?: '))

if version != 6 and version != 7:
    mm = 602000000000000000000000 
    H = 1.008
    He = 4.003
    Li = 6.939
    Be = 9.012
    B = 10.811
    C = 12.011
    N = 14.0067
    O = 15.9994
    F = 18.9984
    Ne = 20.180
    Na = 22.9898
    Mg = 24.305
    Al = 26.9815
    Si = 28.086
    P = 30.086
    S = 32.064
    Cl = 35.453
    Ar = 39.948
    K = 39.098
    Ca = 40.08
    Sc = 44.956
    Ti = 47.9
    V = 50.942
    Cr = 51.996
    Mn = 54.938
    Fe = 55.847
    Co = 55.933
    Ni = 58.69
    Cu = 63.54
    Zn = 65.37
    Ga = 69.72
    Ge = 72.59
    As = 74.922
    Se = 78.96
    Br = 79.904
    Kr = 83.80
    #not in order \/
    Sr = 87.62
    Ag = 107.870
    Sn = 118.69
    Sb = 121.76
    Au = 196.967
    Bi = 207.19
    Hg = 200.59

    num = int(input('how many elements(0 for N/A): '))
    compos = []
    nums = []

    total = 0
    for i in range(num):
        compos1 = input('element: ')
        nums1 = float(input('amount: '))
        compos.append(compos1)
        nums.append(nums1)
        total = total + nums[i]

if version == 1:
  num11 = 0 #calc total number of atoms
  for i in range(num):
    num11 = num11 + nums[i]
    
  print('Total number of atoms = '+str(num11))
  for i in range(num):
    print(compos[i]+': '+str(round(nums[i]))+'/'+str(round(num11))+' = '+str(round(nums[i]/total*100, 1))+ '%')  #round

if version == 2:
    M = input('what is the Molar mass?: ')
    n = input('How many moles are there?: ')
    m = input('What is the mass?: ')
    if m != '':
        if m[len(m)-1] == 'g':
                m = m[:-1]
    Nne = input('How many molecules are there?: ')

    def nf():
        if M != '' and m != '':
            print('n = m/M')
            print('n = '+str(round(float(m),3))+'g/'+str(round(float(M),2))+'g/mol')
            n = float(m)/float(M)
            print('n = '+str(round(float(n),2))+'moles')
            return(n)
        elif Nne != '':
            print ('n = N/(6.02*10^23)')
            print ('n = '+str(round(float(Nne)))+'/(6.02*10^23)')
            n = float(Nne)/mm
            print ('n = '+str(round(float(n),2))+'moles')
            return(n)
        else:
            return('')
    def mf():
        if M != '' and n != '':
            print('m = M*n')
            print('m = '+str(round(float(M),3))+'g/mol*'+str(round(float(n),2))+'mol')
            m = float(M)/float(n)
            print('m = '+str(round(float(n),2))+'g')
            return(m)
        else:
            return('')
    def Mf():
        if num > 0:
            print('M',end="")
            for i in range(num):
                print(compos[i]+str(round(nums[i])),end="")
                print(' = ',end="")
            for i in range(num):
                if i != num-1:
                    print(str(round(nums[i]))+'M'+compos[i]+'+',end="")
                else:
                    print(str(round(nums[i]))+'M'+compos[i])
            total2 = 0
            print('     = ',end="")
            for ii1 in range(num):
                element = globals()[compos[ii1]]
                print(str(round(nums[i]))+'('+str(round(element,2))+')',end="")
                if ii1 != num-1:
                    print('+',end="")
                total2 = total2 + element*nums[ii1]
                M = total2
            print('')
            print('     = '+str(round(total2,2)))
            return(total2)
        elif m != '' and n != '':
            print('M = m/n')
            print('M = '+str(round(float(m),3))+'g/'+str(round(float(n),2))+'mol')
            M = (float(m)/float(n))
            print('M = '+str(round(float(n),2))+'g/mol')
            return(M)
        else:
            return('')

    def Nnef():
        if n != '':
            Nne = int(round(float(n)*mm))
            print('N = n*(6.02*10^23)')
            print('N = '+str(round(float(n),2))+'*(6.02*10^23)')
            Nne = str(Nne)
            print('N = '+str(Nne[0])+'.'+str(Nne[1:4])+'e+'+str(len(Nne)-1))
            Nne = int(Nne)
            return(Nne)
        else:
            return('')
    
    def getall():
        for i in range(5):
            if M == '':
                M = Mf()
            if m == '':
                m = mf()
            if n == '':
                n = nf()
            if Nne == '':
                Nne = Nnef()
                
    print('')
    print('')
    if Nne != '' and n == '':
        n = nf()
        print('')
    if n != '' and m != ''and M == '':
        M = Mf()
        print('')
    elif num != '0' and M == '':
        M = Mf()
        print('')
    if M != '' and m != ''and n == '':
        n = nf()
        print('')
    if M != '' and n != '' and m == '':
        m = mf()
        print('')
    if n != '' and Nne == '':
        Nne = Nnef()
    
    print('M:', M)
    print('n:', n)
    print('m:', m)
    Nne = float(Nne)
    print('N: %g'%Nne)

if version == 3:
    masgram = input('How much does the sample weigh? (g/moles): ')
    
    num34 = 0
    for i in range(num):
	    num34 = num34 + nums[i]

    if num34 > 95 and num34 < 105:
        print('Assume 100g of sample: ', end="")
        for i in range(num):
            print(str(nums[i]) + 'g ' + compos[i], end="")
            if i != num-1:
                print(', ', end="")
        print('')
        print('Calculate the number of Moles')
        for i in range(num):
            element = globals()[compos[i]]
            print(compos[i] + ': ' + str(nums[i])+ 'g/'+ str(round(element, 3)) + 'g/mol = ', end="")
            nums[i] = float(nums[i])/element
            print('%.3f moles' % nums[i])

        print('Divide by the smallest:')
        smallest = 1000.0
        for i in range(num):
            if nums[i] < smallest:
                smallest = nums[i]
    
        for i in range(num):
            print(compos[i] + ': ' + '%.3f'%nums[i] + 'mol/' + '%.3f'%smallest + 'mol = ', end="")
            nums[i] = round(nums[i]/smallest, 2)
            print(nums[i])

        temp2 = 1
        temp3 = 1
        for i in range(num):
            temp = round(nums[i])
            temp = abs(temp-nums[i])
            if temp >= 0.28 and temp <= 0.39:
                temp3 = 3
            elif temp > 0.39 and temp <= 0.55:
                temp2 = 2
            elif temp >= 0.55 and temp <= 0.72:
                temp3 = 3
        temp = temp2*temp3
    
        print(compos[0], end="")
        for i in range(1, num):
            print(':' + compos[i], end="")
    
        print(', ', end="")
    
        for i in range(num):
            nums[i] = round(nums[i]*temp)
            print(nums[i], end="")
            if i != num-1:
                print(':', end="")
        print('')


    print('Empirical formula: ', end="")
    for i in range(num):
        print(compos[i]+str(round(nums[i])), end="") #does this need round
    print('')
    if masgram != '':
      num33 = 0
    
      for i in range(num):
        element = globals()[compos[i]]
        num33 = element*nums[i] + num33

      print('M', end="")
      for i in range(num):
        print(compos[i]+str(round(nums[i])), end="")#more round
      print(' = ', end="")
  
      if nums[0] != 1:
		      print(str(round(nums[0]))+'M'+compos[0], end="")#bit more here
      if nums[0] == 1:
		      print('M'+compos[0], end="")

      for i in range(1, num):
	      if nums[i] != 1:
		      print('+'+str(round(nums[i]))+'M'+compos[i], end="")#bit more here
	      elif nums[i] == 1:
		      print('+'+'M'+compos[i], end="")
      print('')
      print('     =', str(round(num33, 3)))

      print('differences in mass: ')
      for i in range(num):
	      print(str(masgram)+'/'+str(round(num33, 3))+'='+str(round(float(masgram)/num33)))

      print('Molecular formula: ', end="")
      num33 = round(float(masgram)/num33)
      for i in range(num):
        nums[i] = nums[i]*num33
        print(compos[i]+str(round(nums[i])), end="") #does this need round?

if version == 4:
  num11 = 0 #calc total molecular mass
  for i in range(num):
    element = globals()[compos[i]]
    num11 = num11 + element*nums[i]
    
  print('Total molecular mass = '+ str(round(num11, 3)))
  for i in range(num):
    element = globals()[compos[i]]
    print(compos[i]+': '+str(round(element*nums[i], 3))+'/'+str(round(num11, 3))+' = '+str(round(element*nums[i]/round(num11, 3)*100, 3))+ '%')  #round

if version == 5:
    #equation = input('input the ratio: ')
    if compos[0] != '':
        num = int(input('how many molecules are there?: '))
        temp1 = nums
        temp2 = compos
        nums = [[] for i in range(num)]
        compos = [[] for i in range(num)]
        nums[0] = temp1
        compos[0] = temp2
        
        for i in range(1,num):
            total = int(input('how many elements?: '))
            for i2 in range(total):
                compos1 = input('element: ')
                nums1 = float(input('amount: '))
                compos[i].append(compos1)
                nums[i].append(nums1)    

        M = ['' for i in range(num)]

        for i in range(num):
            total = 0
            for i2 in range(len(nums[i])):
                element = globals()[compos[i][i2]]
                print(compos)
                print(element, compos[i][i2])
                total = total + int(nums[i][i2])*element
            M[i] = round(total,3)
            print (total, '-')

        print (M)
    
    
    while num != 0 and compos[0] == '':
        num = float(input('what is the number: '))
        num2 = int(input('which number is it for?: '))-1
        num = float(num/float(nums[num2]))
        for i in range(len(nums)):
            print(float(nums[i])*num,' ',end="")
        print('')
    while num != 0 and compos[0] != '':
        num = input('what is the number: ')
        num2 = int(input('which number is it for?: '))-1
        if num[len(num)-1] == 'g':
            num = float(num[:-1])
            num = num/M[num2]
        for i in range(len(nums)):
            print(round(M[i]*float(num),3),' ',end="")
        print('')

        
while version == 6:
    x = int(input('how many isotopes are there? '))

    p = [[] for i in range(x)]
    m = [[] for i in range(x)]
    for i in range(x):
        p[i] = float(input('what is the ' + str(i+1) + ' percent? '))
        m[i] = float(input('what is the ' + str(i+1) + ' mass? '))

    ans = 0
    for i in range(x):
        ans = ans + p[i]*m[i]

    temp = 0
    for i in range(x):
        temp = temp + p[i] 
    if temp > 50:
        ans = ans/100
    print(ans)

while version == 7:
    n = [[],[]]
    x = float(input('what is the average atomic mass? '))
    n[0] = float(input('What is the first mass? '))
    n[1] = float(input('What is the second mass? '))
    answer = (x - n[1])/(n[0]-n[1])
    print (str((float(answer))*100) + '% of the first isotope')
    print (str((1-float(answer))*100) + '% of the second isotope')




