# -*- coding: utf-8 -*-
import copy, codecs


class Tree:
    def __init__(self, data=u''):
        self.parent = None
        self.children = []
        self.data = data
        if self.parent == None:
            self.name = 'I am root'
            self.root = self

    def grow_leaf(self, data=u''):
        child = Tree(data)
        child.parent = self
        self.children.append(child)
        child.name = str(self.name) + "'s child #" + str(self.children.index(child) + 1)
        return child

    def kill_a_child(self, child):
        if child.children != []:
            for i in child.children:
                child.kill_a_child(i)
        self.children.remove(child)

    def path_to_root(self, papa=None):
        path = [self]
        if papa==None:
            papa=self
        while papa.parent != None:
            path.append(papa.parent)
            papa = papa.parent
        return path

    # def path_to_node(self, other):
    #     path=[]
    #     arr=[]
    #     arr2=[]
    #     not_a_path=[]
    #     path1=self.path_to_root()
    #     d=0
    #     path2=other.path_to_root()
    #     for i in path1:
    #         if i not in path2:
    #             print '___'+i.data
    #             path.append(i)
    #     for n in path2:
    #         if n not in path1:
    #             arr.append(n)
    #     path.append(arr2[-1].parent)
    #     path.append(sorted(arr, reverse=True))
    #     return path

    def path_to_node1(self, other):
        arr = []
        final_path = []
        path = self.path_to_root()
        path2 = other.path_to_root()
        for i in path:
            if i not in path2:
                final_path.append(i)
        for i in path2:
            if i not in path:
                arr.append(i)
        a = len(final_path) - 1
        new_root = final_path[a].parent
        final_path.append(new_root)
        final_path += arr[::-1]
        return final_path

    def leaves(self, child=None):
        l = []
        if child == None:
            child = self
        if child.children == []:
            l.append(child)
        for i in child.children:
            l += self.leaves(i)
        return l

    def search(self, data, results=[]):
        if self.data == data:
            results.append(self)
        if self.children != None:
            for i in self.children:
                i.search(data)
        return results

    def tree_walk(self):
        for i in self.children:
            for n in i.tree_walk():
                yield n
        yield self

    def level(self, lvl):
        for i in self.tree_walk():
            if len(i.path_to_root())==lvl+1:
                yield i


class Relative(Tree):
    def givebirth(self, data=u''):
        child = Relative(data)
        child.parent = self
        self.children.append(child)
        child.name = str(self.name) + "'s child #" + str(self.children.index(child) + 1)
        return child

    def findbrothers(self):
        brothers = self.parent.children[:]
        brothers.remove(self)
        return brothers

    def finddad(self):
        return self.parent

    def findchildren(self):
        return self.children

    def finduncles(self):
        uncles = self.parent.parent.children[:]
        uncles.remove(self.parent)
        return uncles

    def findgrandchildren(self):
        grandchildren = []
        for i in self.children:
            for n in i.children:
                grandchildren.append(n)
        return grandchildren

    def findcousins(self):
        cousins = []
        for i in self.finduncles():
            for n in i.children:
                cousins.append(n)
        return cousins

    def findnephews(self):
        nephews = []
        for i in self.findbrothers():
            for n in i.children:
                nephews.append(n)
        return nephews


grandpa = Relative('Abraham')
a = grandpa.givebirth('Isaak')
b = grandpa.givebirth('Ishmael')
d = a.givebirth('Esau')
c = a.givebirth('Jakob')
# print a.finddad().data
# print a.name, a.data
kids = []
for i in range(12):
    kids.append(c.givebirth())
kids[10].data = 'Joseph'
kids[11].data = 'Benjamin'
e = kids[11].givebirth('Abraham2')
for i in e.path_to_root():
    print i.data
print ''
# for i in e.path_to_root():
#     print i.data
#for i in d.path_to_node1(e):
    #print i.data
# for i in e.path_to_node(d):
    #     print i.data
for i in grandpa.tree_walk():
    print i.name
print ''
for i in grandpa.level(1):
    print i.name