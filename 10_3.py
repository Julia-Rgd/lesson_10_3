import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            amount = random.randint(50, 500)
            self.balance += amount
            print(f"Пополнение: {amount}. Баланс: {self.balance}")
            time.sleep(0.001)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
                print("Замок разблокирован")
    def take(self):
        for i in range(100):
            amount = random.randint(50, 500)
            print(f"Запрос на {amount}")
            if amount <= self.balance:
                self.balance -= amount
                print(f"Снятие: {amount}. Баланс: {self.balance}")
        else:
            print("Запрос отклонен, недостаточно средств")
            self.lock.acquire()

        time.sleep(0.001)

if __name__ == "__main__":
    bk = Bank()
    th1 = threading.Thread(target=Bank.deposit, args=(bk,))
    th2 = threading.Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print(f'Итоговый баланс: {bk.balance}')

"C:\Users\User\PycharmProjects\HELLO WORLD\.venv\Scripts\python.exe" "C:\Users\User\PycharmProjects\HELLO WORLD\module_10_3.py" 
Пополнение: 374. Баланс: 374
Запрос на 104
Снятие: 104. Баланс: 270
Запрос на 140
Снятие: 140. Баланс: 130
Запрос на 378
Запрос на 346
Запрос на 432
Запрос на 51
Снятие: 51. Баланс: 79
Запрос на 410
Запрос на 185
Запрос на 340
Запрос на 135
Запрос на 467
Запрос на 212
Запрос на 266
Запрос на 321
Запрос на 179
Запрос на 322
Запрос на 120
Запрос на 349
Запрос на 94
Запрос на 145
Запрос на 81
Запрос на 432
Запрос на 108
Запрос на 133
Запрос на 296
Запрос на 209
Запрос на 53
Снятие: 53. Баланс: 26
Запрос на 116
Запрос на 69
Запрос на 221
Запрос на 127
Запрос на 376
Запрос на 296
Запрос на 243
Запрос на 468
Запрос на 278
Запрос на 150
Запрос на 213
Запрос на 271
Запрос на 183
Запрос на 350
Запрос на 174
Запрос на 319
Запрос на 441
Запрос на 286
Запрос на 163
Запрос на 129
Запрос на 461
Запрос на 484
Запрос на 407
Запрос на 102
Запрос на 425
Запрос на 148
Запрос на 422
Запрос на 208
Запрос на 111
Запрос на 78
Запрос на 491
Запрос на 205
Запрос на 132
Запрос на 455
Запрос на 112
Запрос на 253
Запрос на 444
Запрос на 194
Запрос на 258
Запрос на 127
Запрос на 427
Запрос на 161
Запрос на 214
Запрос на 135
Запрос на 236
Запрос на 160
Запрос на 183
Запрос на 355
Запрос на 226
Запрос на 405
Запрос на 484
Запрос на 381
Запрос на 138
Запрос на 233
Запрос на 299
Запрос на 131
Запрос на 486
Запрос на 421
Запрос на 57
Запрос на 355
Запрос на 70
Запрос на 59
Запрос на 247
Запрос на 258
Запрос на 196
Запрос на 252
Запрос на 318
Запрос на 438
Запрос на 94
Запрос на 256
Запрос на 406
Запрос на 408
Запрос на 198
Запрос отклонен, недостаточно средств
Пополнение: 476. Баланс: 502
Замок разблокирован
Пополнение: 470. Баланс: 972
Пополнение: 454. Баланс: 1426
Пополнение: 120. Баланс: 1546
Пополнение: 466. Баланс: 2012
Пополнение: 477. Баланс: 2489
Пополнение: 307. Баланс: 2796
Пополнение: 61. Баланс: 2857
Пополнение: 432. Баланс: 3289
Пополнение: 407. Баланс: 3696
Пополнение: 192. Баланс: 3888
Пополнение: 421. Баланс: 4309
Пополнение: 417. Баланс: 4726
Пополнение: 196. Баланс: 4922
Пополнение: 134. Баланс: 5056
Пополнение: 313. Баланс: 5369
Пополнение: 238. Баланс: 5607
Пополнение: 454. Баланс: 6061
Пополнение: 425. Баланс: 6486
Пополнение: 220. Баланс: 6706
Пополнение: 444. Баланс: 7150
Пополнение: 227. Баланс: 7377
Пополнение: 143. Баланс: 7520
Пополнение: 188. Баланс: 7708
Пополнение: 363. Баланс: 8071
Пополнение: 319. Баланс: 8390
Пополнение: 123. Баланс: 8513
Пополнение: 56. Баланс: 8569
Пополнение: 88. Баланс: 8657
Пополнение: 117. Баланс: 8774
Пополнение: 147. Баланс: 8921
Пополнение: 120. Баланс: 9041
Пополнение: 491. Баланс: 9532
Пополнение: 304. Баланс: 9836
Пополнение: 393. Баланс: 10229
Пополнение: 85. Баланс: 10314
Пополнение: 202. Баланс: 10516
Пополнение: 419. Баланс: 10935
Пополнение: 404. Баланс: 11339
Пополнение: 51. Баланс: 11390
Пополнение: 174. Баланс: 11564
Пополнение: 128. Баланс: 11692
Пополнение: 465. Баланс: 12157
Пополнение: 91. Баланс: 12248
Пополнение: 378. Баланс: 12626
Пополнение: 149. Баланс: 12775
Пополнение: 220. Баланс: 12995
Пополнение: 436. Баланс: 13431
Пополнение: 318. Баланс: 13749
Пополнение: 214. Баланс: 13963
Пополнение: 152. Баланс: 14115
Пополнение: 467. Баланс: 14582
Пополнение: 352. Баланс: 14934
Пополнение: 220. Баланс: 15154
Пополнение: 265. Баланс: 15419
Пополнение: 157. Баланс: 15576
Пополнение: 227. Баланс: 15803
Пополнение: 154. Баланс: 15957
Пополнение: 424. Баланс: 16381
Пополнение: 286. Баланс: 16667
Пополнение: 414. Баланс: 17081
Пополнение: 283. Баланс: 17364
Пополнение: 483. Баланс: 17847
Пополнение: 102. Баланс: 17949
Пополнение: 172. Баланс: 18121
Пополнение: 462. Баланс: 18583
Пополнение: 120. Баланс: 18703
Пополнение: 213. Баланс: 18916
Пополнение: 199. Баланс: 19115
Пополнение: 273. Баланс: 19388
Пополнение: 319. Баланс: 19707
Пополнение: 310. Баланс: 20017
Пополнение: 245. Баланс: 20262
Пополнение: 332. Баланс: 20594
Пополнение: 198. Баланс: 20792
Пополнение: 220. Баланс: 21012
Пополнение: 124. Баланс: 21136
Пополнение: 342. Баланс: 21478
Пополнение: 448. Баланс: 21926
Пополнение: 478. Баланс: 22404
Пополнение: 111. Баланс: 22515
Пополнение: 182. Баланс: 22697
Пополнение: 163. Баланс: 22860
Пополнение: 498. Баланс: 23358
Пополнение: 168. Баланс: 23526
Пополнение: 296. Баланс: 23822
Пополнение: 55. Баланс: 23877
Пополнение: 432. Баланс: 24309
Пополнение: 100. Баланс: 24409
Пополнение: 194. Баланс: 24603
Пополнение: 483. Баланс: 25086
Пополнение: 222. Баланс: 25308
Пополнение: 406. Баланс: 25714
Пополнение: 122. Баланс: 25836
Пополнение: 344. Баланс: 26180
Пополнение: 287. Баланс: 26467
Пополнение: 490. Баланс: 26957
Пополнение: 305. Баланс: 27262
Пополнение: 291. Баланс: 27553
Итоговый баланс: 27553

Process finished with exit code 0
