// Dates converter Parser

class Timestamp{
    __appendZero(d){
        return d < 10 ? `0${d}` : d;
    }

    get now(){ return new Date().getTime() }

    toString(timestamp, is_am = true){
        let d

        if(timestamp instanceof Date){
            d = timestamp
        }else{
            d = new Date(timestamp)
        }
        
        const day       = this.__appendZero(d.getDate())
        const month     = this.__appendZero(d.getMonth() + 1)
        const year      = d.getFullYear();
    
        let hour        = this.__appendZero(d.getHours())
        const minutes   = this.__appendZero(d.getMinutes())
        const seconds   = this.__appendZero(d.getSeconds())
    
    
        if (is_am){
            let is_am = "AM"
    
            if(hour > 12){
                hour = this.__appendZero(hour - 12)
                is_am = "PM"
            }
    
            return [`${day}.${month}.${year} - ${hour}:${minutes}:${seconds} ${is_am}`, d.toString()]
        }
        return [`${day}.${month}.${year} - ${hour}:${minutes}:${seconds} H`, d.toString()]
    }
}

class Dates{
    get timestamp(){
        return new Timestamp()
    }

    getNMonthsAgo(n){
        const now = new Date()
        now.setMonth(now.setMonth() - n)
        return this.timestamp.toString(now)
    }

    getNDaysAgo(n){
        const now = new Date()
        now.setDate(now.getDate() - n)
        return this.timestamp.toString(now)
    }

    getNHoursAgo(n){
        const now = new Date()
        now.setHours(now.getHours() - n)
        return this.timestamp.toString(now)
    }

    getNMinutesAgo(n){
        const now = new Date()
        now.setMinutes(now.getMinutes() - n)
        return this.timestamp.toString(now)
    }

    getNSecondsAgo(n){
        const now = new Date()
        now.setSeconds(now.getSeconds() - n)
        return this.timestamp.toString(now)
    }

    stringToTimestamp(date_string){
        return new Date(date_string).getTime()
    }
}

class Uniques{
    find(arr){
        const tmp = []
        arr.forEach(x => {
            if(tmp.indexOf(x) === -1){
                tmp.push(x)
            }
        });
        return tmp
    }

    findArrayByValue(arr, value){
        return arr.filter(x => {
            if(x instanceof Array){
                let i = 0;

                for(; i < x.length; i++){
                    if(x[i] === value){
                        return x
                    }
                }

            }
        })
    }

    findByValue(arr, value){
        return arr.filter(x => {
            if (x === value){
                return x
            }
        })
    }

    count(arr){
        const uniques = {}

        const checkUnique = (x) => {
            if(uniques[x] === undefined){
                uniques[x] = 1
            }else{
                uniques[x] += 1
            }
        }

        arr.forEach(x => {
            if(x instanceof Array){
                x.forEach(y => {
                    checkUnique(y)
                })
            }else{
                checkUnique(y)
            }
           
        })

        return uniques
    }
}


class Utils{
    get dates(){ return new Dates() }
    get uniques(){ return new Uniques() }
}

// Only use utils class !!


// function main(){
//     // const dates = new Dates()
//     // // console.log(dates.timestamp.toString(dates.timestamp.now, "24h"))
//     // // console.log(dates.timestamp.getNDays(50))
//     // // console.log(dates.timestamp.getNHoursAgo(48));
//     // const [_, days_ago] = dates.getNDaysAgo(1)
//     // console.log(dates.stringToTimestamp(days_ago))
//     // const uniques = new Uniques()
//     // const data = [['asd', 'sdfsf', 'asd'],['asd', 'zxc'], ['asd', 'jeds', 'zxc'], ['jads', 'asdasd']]  
//     // const data = ['asd', 'sdfsf', 'asd','asd', 'zxc', 'asd', 'jeds', 'zxc', 'jads', 'asdasd']  
//     // console.log(uniques.count(data))
//     // const d = uniques.findByValue(data, "asd")
//     // console.log(d)
// }
// main();