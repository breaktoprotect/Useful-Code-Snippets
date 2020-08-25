import multiprocessing as mp
import random
import time

def a_function(L, i):
	delay = random.randint(1,1)
	time.sleep(delay)
	L.append('Process {I} appended! ({DELAY} seconds)'.format(I=i, DELAY=delay))
	print("[+] Process {I} appended in {DELAY} seconds".format(I=i, DELAY=delay))
	return
	
def main():
	pool = mp.Pool(processes=2)
	manager = mp.Manager()
	L = manager.list()
	
	processes = []
	
	for i in range(5):
		pool.apply_async(a_function, args=(L,i))
	pool.close()
	
	print(pool.__dict__)
	
	# Inspect current processes waiting
	while (len(pool._cache) > 0):
		time.sleep(1)
		print("[*] Current pool._cache:" + str(pool._cache))
		
	# Blocks until all processes are completed
	pool.join()
	
	print(L)
	print("[+] Program ended.")
		
if __name__ == "__main__":
	main()
