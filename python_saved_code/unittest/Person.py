class Person ():
    name_ls = []

    def set_name(self, new_name: str):
        self.name_ls.append (new_name)
        return len (self.name_ls) - 1  # returning index

    def get_name(self, ind: int):
        if ind < len (self.name_ls):
            return self.name_ls[ind]
        else:
            return None


if __name__ == '__main__':
    myperson = Person ()

    print ('User xyz has been added with id ', myperson.set_name ('xyz'))
    print ('User abc has been added with id ', myperson.set_name ('abc'))

    print ('User associated with id 0 is ', myperson.get_name (0))
    print ('User associated with id 1 is ', myperson.get_name (1))

    print ('User associated with id 0 is ', myperson.get_name (17))
    print (myperson.name_ls)
