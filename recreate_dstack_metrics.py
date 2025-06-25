print("""\
NAME                 CPU     MEMORY
ray-cluster-ppo
  replica=0 job=0     6%     129710MB/2324160MB     #0  41832MB/196608MB   21% Util
                                                  #1  41378MB/196608MB   21% Util
                                                  #2  41378MB/196608MB   21% Util
                                                  #3  40898MB/196608MB   21% Util
                                                  #4  41282MB/196608MB   21% Util
                                                  #5  41378MB/196608MB   21% Util
                                                  #6  41386MB/196608MB   21% Util
                                                  #7  39850MB/196608MB   20% Util

  replica=0 job=1     5%     117249MB/2324160MB     #0  29732MB/196608MB   15% Util
                                                  #1  29884MB/196608MB   15% Util
                                                  #2  29884MB/196608MB   15% Util
                                                  #3  29404MB/196608MB   15% Util
                                                  #4  29844MB/196608MB   15% Util
                                                  #5  29494MB/196608MB   15% Util
                                                  #6  29948MB/196608MB   15% Util
                                                  #7  28468MB/196608MB   14% Util
""")

