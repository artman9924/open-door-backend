2025-04-30T14:08:14.58350844Z 127.0.0.1 - - [30/Apr/2025:14:08:14 +0000] "OPTIONS /post-message HTTP/1.1" 200 0 "https://lustrous-malabi-115908.netlify.app/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0"
2025-04-30T14:08:14.967426594Z Message received: 'Thanks for checking out the app!' | Flagged: False
2025-04-30T14:08:14.967445666Z 127.0.0.1 - - [30/Apr/2025:14:08:14 +0000] "POST /post-message HTTP/1.1" 200 57 "https://lustrous-malabi-115908.netlify.app/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0"
2025-04-30T14:08:17.664908214Z 127.0.0.1 - - [30/Apr/2025:14:08:17 +0000] "GET /get-messages HTTP/1.1" 200 102 "https://lustrous-malabi-115908.netlify.app/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0"
2025-04-30T14:13:07.580501927Z 127.0.0.1 - - [30/Apr/2025:14:13:07 +0000] "GET /get-messages HTTP/1.1" 200 102 "https://lustrous-malabi-115908.netlify.app/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0"
2025-04-30T14:13:28.305105293Z 127.0.0.1 - - [30/Apr/2025:14:13:28 +0000] "GET /admin?key=pass1029 HTTP/1.1" 200 397 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0"
2025-04-30T14:13:47.593148844Z 127.0.0.1 - - [30/Apr/2025:14:13:47 +0000] "GET /get-messages HTTP/1.1" 200 102 "https://lustrous-malabi-115908.netlify.app/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0"
2025-04-30T14:17:36.083433904Z 127.0.0.1 - - [30/Apr/2025:14:17:36 +0000] "GET /get-messages HTTP/1.1" 200 102 "https://lustrous-malabi-115908.netlify.app/" "Mozilla/5.0 (iPhone; CPU iPhone OS 18_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/22E252 [FBAN/FBIOS;FBAV/510.0.0.38.93;FBBV/724276253;FBDV/iPhone16,2;FBMD/iPhone;FBSN/iOS;FBSV/18.4.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/728339409;IABMV/1]"
2025-04-30T14:32:17.220724366Z 127.0.0.1 - - [30/Apr/2025:14:32:17 +0000] "GET /get-messages HTTP/1.1" 200 102 "https://lustrous-malabi-115908.netlify.app/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0"
2025-04-30T14:38:13.600275955Z 127.0.0.1 - - [30/Apr/2025:14:38:13 +0000] "GET /get-messages HTTP/1.1" 200 102 "https://lustrous-malabi-115908.netlify.app/" "Mozilla/5.0 (Linux; Android 14; SM-S918U Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/135.0.7049.110 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/456.0.0.7.52;FBCX/modulariab;]"
2025-04-30T14:41:50.09518335Z 127.0.0.1 - - [30/Apr/2025:14:41:50 +0000] "GET /get-messages HTTP/1.1" 200 102 "https://lustrous-malabi-115908.netlify.app/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0"
2025-04-30T14:57:50.419168658Z [2025-04-30 14:57:50 +0000] [66] [INFO] Handling signal: term
2025-04-30T14:57:50.419561214Z [2025-04-30 14:57:50 +0000] [67] [INFO] Worker exiting (pid: 67)
2025-04-30T14:57:50.91999809Z [2025-04-30 14:57:50 +0000] [66] [INFO] Shutting down: Master
2025-04-30T14:57:50.920037023Z Database already exists.
2025-04-30T14:57:50.920043163Z Added 'flagged' column to messages table.
2025-04-30T15:08:48.64746004Z ==> Running 'gunicorn app:app'
2025-04-30T15:08:51.632209378Z [2025-04-30 15:08:51 +0000] [66] [INFO] Starting gunicorn 23.0.0
2025-04-30T15:08:51.632569566Z [2025-04-30 15:08:51 +0000] [66] [INFO] Listening at: http://0.0.0.0:10000 (66)
2025-04-30T15:08:51.632651407Z [2025-04-30 15:08:51 +0000] [66] [INFO] Using worker: sync
2025-04-30T15:08:51.636361966Z [2025-04-30 15:08:51 +0000] [67] [INFO] Booting worker with pid: 67
2025-04-30T15:08:55.527266871Z Database already exists.
2025-04-30T15:08:55.527294502Z Added 'flagged' column to messages table.
2025-04-30T15:08:55.527299742Z 127.0.0.1 - - [30/Apr/2025:15:08:55 +0000] "GET /get-messages HTTP/1.1" 200 3 "https://lustrous-malabi-115908.netlify.app/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0"
2025-04-30T15:08:55.602146077Z 127.0.0.1 - - [30/Apr/2025:15:08:55 +0000] "GET /get-messages HTTP/1.1" 200 3 "https://lustrous-malabi-115908.netlify.app/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0"
2025-04-30T15:08:55.944812607Z 127.0.0.1 - - [30/Apr/2025:15:08:55 +0000] "GET /get-messages HTTP/1.1" 200 3 "https://lustrous-malabi-115908.netlify.app/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0"
2025-04-30T15:08:56.147090253Z 127.0.0.1 - - [30/Apr/2025:15:08:56 +0000] "GET /get-messages HTTP/1.1" 200 3 "https://lustrous-malabi-115908.netlify.app/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0"
2025-04-30T15:08:57.198096429Z 127.0.0.1 - - [30/Apr/2025:15:08:57 +0000] "GET /get-messages HTTP/1.1" 200 3 "https://lustrous-malabi-115908.netlify.app/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0"
2025-04-30T15:10:03.218761199Z 127.0.0.1 - - [30/Apr/2025:15:10:03 +0000] "GET / HTTP/1.1" 404 207 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0"
2025-04-30T15:10:09.512054Z 127.0.0.1 - - [30/Apr/2025:15:10:09 +0000] "GET /get-messages HTTP/1.1" 200 3 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0"
2025-04-30T15:10:42.630641574Z 127.0.0.1 - - [30/Apr/2025:15:10:42 +0000] "OPTIONS /post-message HTTP/1.1" 200 0 "https://lustrous-malabi-115908.netlify.app/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0"
2025-04-30T15:10:42.957390976Z Message received: 'hello!' | Flagged: False
2025-04-30T15:10:42.957413766Z 127.0.0.1 - - [30/Apr/2025:15:10:42 +0000] "POST /post-message HTTP/1.1" 200 57 "https://lustrous-malabi-115908.netlify.app/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0"
2025-04-30T15:10:45.254290463Z 127.0.0.1 - - [30/Apr/2025:15:10:45 +0000] "GET /get-messages HTTP/1.1" 200 76 "https://lustrous-malabi-115908.netlify.app/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0"
2025-04-30T15:26:45.526909796Z [2025-04-30 15:26:45 +0000] [66] [INFO] Handling signal: term
2025-04-30T15:26:45.527722993Z [2025-04-30 15:26:45 +0000] [67] [INFO] Worker exiting (pid: 67)
2025-04-30T15:26:45.928183837Z [2025-04-30 15:26:45 +0000] [66] [INFO] Shutting down: Master
2025-04-30T15:26:45.928219948Z Database already exists.
2025-04-30T15:26:45.928225388Z Added 'flagged' column to messages table.
2025-05-01T00:53:44.03790057Z ==> Running 'gunicorn app:app'
2025-05-01T00:53:47.32465798Z [2025-05-01 00:53:47 +0000] [66] [INFO] Starting gunicorn 23.0.0
2025-05-01T00:53:47.325040106Z [2025-05-01 00:53:47 +0000] [66] [INFO] Listening at: http://0.0.0.0:10000 (66)
2025-05-01T00:53:47.325063918Z [2025-05-01 00:53:47 +0000] [66] [INFO] Using worker: sync
2025-05-01T00:53:47.399899173Z [2025-05-01 00:53:47 +0000] [67] [INFO] Booting worker with pid: 67
2025-05-01T00:53:55.986766203Z Database already exists.
2025-05-01T00:53:55.986802685Z Added 'flagged' column to messages table.
2025-05-01T00:53:55.986807306Z 127.0.0.1 - - [01/May/2025:00:53:55 +0000] "GET /get-messages HTTP/1.1" 200 3 "https://lustrous-malabi-115908.netlify.app/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0"
2025-05-01T00:53:56.116989907Z 127.0.0.1 - - [01/May/2025:00:53:56 +0000] "GET /get-messages HTTP/1.1" 200 3 "https://lustrous-malabi-115908.netlify.app/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0"
2025-05-01T00:53:56.176916665Z 127.0.0.1 - - [01/May/2025:00:53:56 +0000] "GET /get-messages HTTP/1.1" 200 3 "https://lustrous-malabi-115908.netlify.app/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0"
2025-05-01T00:53:56.861756005Z 127.0.0.1 - - [01/May/2025:00:53:56 +0000] "GET /get-messages HTTP/1.1" 200 3 "https://lustrous-malabi-115908.netlify.app/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0"
