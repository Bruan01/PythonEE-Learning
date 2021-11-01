import time
input("欢迎使用“时间管理器！ 按任意键继续 。")
while True:
    task_name = input ("请输入任务名： ")
    task_time = int(input('你觉得自己需要专注几分钟？'))
    start =time.time()##记录现在开始时间
    start_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))##格式化日期
    for t in range(task_time*60,0,-1):
        info = '你还需要继续专注' + str(t) +'秒哦'
        print(info,end = " ")
        print("\b"*(len(info)*2),end = " ",flush = True)
        time.sleep(1)
    print('你已经专注了 %d 分钟，很棒~再加把劲，完成任务！'%task_time)     
    task_status = input('请在完成后输入y； ')
    
    if task_status == 'y':
        end =time.time()
        end_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        actual_time = int((end -start)/60)
        start_end = start_time + '---' + end_time +'\n'  
        with open(r'/time_list.txt', 'a', encoding ='utf-8') as f:
            f.write(task_name + '的预计时长为：'+str(task_time)+'分钟\n') 
            f.write(task_name + '的实际时长为：'+str(actual_time)+'分钟\n')
            choice = input('建立一个新任务请按 y ，退出请按其他键')
            if choice != 'y':
                break
print('愿被你善待的时光，予你美好的回赠。')            