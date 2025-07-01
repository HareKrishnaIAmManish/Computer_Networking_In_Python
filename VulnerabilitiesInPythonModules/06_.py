import pickle
object_list=['mastering','python','security']
with open('data.pickle','wb') as file:
    pickle.dump(object_list,file)
with open('data.pickle','rb') as file:
    data=pickle.Unpickler(file)
    list=data.load()
    print(list)
