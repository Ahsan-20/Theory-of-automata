class DFA:
    
 def valid(input_String):
  for k in range (len(input_String)):
   if input_String[k] not in ['0',"1"]:
    print("Invalid String ==",input_String)
    exit()

 def check(final_state,pas,cur_state):
  size=len(final_state)
  for i in range(size):
   if(cur_state == final_state[i]):
    pas='Accepted'
    break
   else:
    pas='Rejected' 
  if(pas=='Accepted'):
    print("String is Accepted ==",cur_state)
  elif(pas=='Rejected'):
    print("String is Rejected ==",cur_state)


 def start(input_String,current_state,size):
    def q0(input_String):

      if input_String=="0":
        c_state="q3"
      elif input_String=="1":
        c_state="q1"

      return c_state

    def q1(input_String):

      if input_String=="0":
        c_state="q1"
      elif input_String=="1":
        c_state="q2"
      return c_state

    def q2(input_String):

      if input_String=="0":
        c_state="q2"

      elif input_String=="1":
        c_state="q2"
      return c_state



    def q3(input_String):

      if input_String=="0":
        c_state="q4"
      elif input_String=="1":
        c_state="q3"
      return c_state

    def q4(input_String):
      if input_String=="0":
        c_state="q4"
      elif input_String=="1":
        c_state="q4"
      return c_state
    c_state=current_state

    for i in range(size):
      if c_state=="q0":
        c_state=q0(input_String[i])

      elif c_state=="q1":
        c_state=q1(input_String[i])


      elif c_state=="q2":
        c_state=q2(input_String[i])

      elif c_state=="q3":
        c_state=q3(input_String[i])

      elif c_state=="q4":
        c_state=q4(input_String[i])

    return c_state  





def main() :
 dfa=DFA
 states=["q0","q1","q2","q3","q4"]
 start_state="q0"
 final_state=["q2","q4"]
 current_state="q0"
 valid_string=["0","1"]

 select=input("Press 1 to enter a string \nPress 2 to read string from txt file\n")
 if(select=='1'):

  input_String=input("Enter a string ")
  size=len(input_String)
  current_state="q0"
  

  dfa.valid(input_String)
  current_state= dfa.start(input_String, start_state,size)
  dfa.check(final_state,'Rejected',current_state)
 
 elif(select=='2'):
  file = open('t1example.txt', 'r')
  for line in file:
   current_state="q0"
   string=line
   size=len(string)
   current_state= dfa.start(string,start_state ,size-1)
   dfa.check(final_state, 'Rejected', current_state)



if __name__ == "__main__":
    main()