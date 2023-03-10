def parser(result):
    
    result = result.split('\n')
    output = []
    
    for line in result:
        
        line = line.split(' ')
        interval =''
        transfer = 0
        bandwith = 0
        
        for n in range(len(line)):
            if(line[n] == 'sec'):
                interval = line[n-2][2:]+line[n-1]
            elif(line[n] == 'MBytes'):
                transfer = float(line[n-1])
            elif(line[n] == 'Mbits/sec'):
                bandwith = float(line[n-1])
                
        if transfer>0:
            output.append({
                'Interval' : interval,
                'Transfer' : transfer,
                'Bitrate': bandwith
            })
            
    return output
