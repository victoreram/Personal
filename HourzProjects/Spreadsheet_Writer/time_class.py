# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 20:29:21 2016

@author: ramir
"""

#int rem = mins / 60;
#this->minutes_ = this->minutes_ + (mins % 60);
#minutes_ = minutes_ + (mins % 60);
#hours_ = hrs + rem + hours_;

#minutes = total_seconds / 60
#seconds = total_seconds % 60

def time_to_s(time):
    '''given a time, return the total amount of seconds'''
    mi_s = time.minutes * 60
    total_sec = mi_s + time.seconds
    return total_sec

def s_to_time(s):
    mi = int(s // 60)
    sec = int(s % 60)
    #new_time = int_construct
    t_str = str(mi) + ":" + str(sec)
    new_time = Time(t_str)
    return new_time

class Time:
    def __init__(self, time_str="0:00",m=0,s=0):
        #self.__minutes = minutes
        #self.__seconds = seconds
        colon = time_str.index(":")
        self.minutes = int(time_str[:colon])
        self.seconds = int(time_str[colon+1:])
        #m = self.__minutes
        #s = self.__seconds
        
    #def int_construct(self, minutes, seconds):
    #    self.minutes = minutes
    #    self.seconds = seconds
    
    def __str__(self):
        
        min_str = str(self.minutes)
        if self.seconds < 10:
            sec_str = "0" + str(self.seconds)
        else:
            sec_str = str(self.seconds)
            
        time_str = min_str + ":" + sec_str
        return time_str     
        
    def __sub__(self, to_subtract):
        self_sec = time_to_s(self)
        sub_sec = time_to_s(to_subtract)
        new_sec = self_sec - sub_sec
        new_time = s_to_time(new_sec)
        return new_time
    
    def __add__(self, to_add):
        self_sec = time_to_s(self)
        add_sec = time_to_s(to_add)
        new_sec = self_sec + add_sec
        new_time = s_to_time(new_sec)
        return new_time
        
    def __eq__(self, time_2):
        if time_to_s(self) == time_to_s(time_2):
            return True
        else:
            return False
            
    def __ne__(self, time_2):
        if time_to_s(self) != time_to_s(time_2):
            return True
        else:
            return False
            
    def __lt__(self, time_2):
        if time_to_s(self) < time_to_s(time_2):
            return True
        else:
            return False
            
    def __le__(self, time_2):
        if time_to_s(self) <= time_to_s(time_2):
            return True
        else:
            return False 
            
    def __gt__(self, time_2):
        if time_to_s(self) > time_to_s(time_2):
            return True
        else:
            return False
            
    def __ge__(self, time_2):
        if time_to_s(self) >= time_to_s(time_2):
            return True
        else:
            return False
#a = Time("5:10")
#b = Time("3:25")
#c = Time("6:55")
#e = Time("5:10")
#print(a.minutes)
#print(a)
#a.seconds
#b = a.str_to_time()

#d = s_to_time(121)
#print(b-c)