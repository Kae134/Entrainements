jours = [13, 12, 11, 9, 16, 17, 100]

class la_question_est_vite_repondu :
    def __init__(self, jours, dodo):
        self.lst_jours = jours
        self.max_list = len(self.lst_jours)
        self.dodo_cons = dodo
        self.result = []
        self.result_pas_fun = 0

    def algo(self) :
        i = 1
        g_la_reponse = False
        if len(self.lst_jours) <= self.dodo_cons:
            for ele in self.lst_jours :
                        self.result.append('taff')
                        self.result_pas_fun += ele
            g_la_reponse = True

        while g_la_reponse != True :
            if (i+4) >= self.max_list :
                while i <= self.max_list:
                    self.result.append('le taff')
                    self.result_pas_fun += self.lst_jours[i-1]
                    i += 1
                
                
                g_la_reponse = True

            else :
                bubble_with_money = self.lst_jours[i-1:(i+self.dodo_cons-1)]
                min = self.is_min(bubble_with_money, self.lst_jours[i+self.dodo_cons-1])
                if min[0] == True :   
                    for ele in bubble_with_money :
                        if ele == min[1]:
                            try :
                                if self.result[i-2] == 'dodo':
                                    self.result_pas_fun += self.lst_jours[i-1]
                                    self.result.append('taff')
                            except :
                                self.result.append('dodo')
                            i += 1
                            break
                        else :
                            self.result.append('le taff')
                            
                            self.result_pas_fun += self.lst_jours[i-1]
                        i += 1
                else :
                    for y in range(self.dodo_cons):
                        self.result.append('le taff')
                        self.result_pas_fun += self.lst_jours[i-1]
                        i += 1

                    i += 1
                    self.result.append('dodo')
                    
            


    def is_min(self, lst, ele_to_compare):
        min = ele_to_compare

        # boucle dans la liste des ele a compare, si un ele est plus petit que 'ele_to_compare'
        # alors il devient le min
        # si il y a aucun min alors 'ele_to_compare' etait le min

        for ele in lst :   
            if ele < min :
                min = ele
        
        if min != ele_to_compare :
            return [True, min]
        else :
            return [False, min]


test = la_question_est_vite_repondu(jours, 3)

test.algo()
print(test.result)
print(test.result_pas_fun)



