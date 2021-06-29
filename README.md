![](docs/images/datapup.gif)

# puptect your data


#### Premise

Given 45 seconds of login information, what statistics can you generate to show malicious intent?

#### Conclusion

You can't. 

You're expected to be in the shoes of every attacker, and formulate static rules for every type of attack pattern possible. **Static rules is so 2010.**

Baselines, clustering, and network graphs FTW. maybe. 

To show how static rules can be, we will use a simplistic binary classification model to determine, "bad" and "not bad". 
 
Blacklisted IPs will be "bad."



### dependencies
- docker

### bulid
```shell
./docker/build.sh
```

### test
```shell
./docker/test.sh
```

### run
```shell
./docker/run.sh
```


#### Lessons learned

Creating complex rules to cover complex attack patterns are the norm, because we're thinking within the boundaries of human capabilities. Every analyst requires the collective knowledge of all patterns, all methods, and all potential future methods; and would still be lacking the insights to novel tactics. Need more proof? See Nature 550,354–359 (2017)


#### Take aways

As a human analyst, you see things that are "out of the norm", like:
- misspelled user agent strings
- non-typical agent string formats
- device type changes

And simple things, like:
- multiple failed logins using similar source code, that uses the same agent string
- bot hopping to avoid IP blocking when logging in gets 401'ed

Ideally, the real challenge is, "how do you detect when everything looks how it should be?"

That's the real inside threat.


#### Next steps

- better third party enrichments
- better statistical models
- resolve geoip locations
- attribute user agent strings 

## Example

alerts:
```shell
>>> [print(x) for x in alerts]
  userid event_type status_code             ip                                          useragent  blacklisted
0   john      login         200  109.184.11.34  mozilla/5.0 (linux; android 6.0.1; redmi note ...         True
  userid event_type status_code            ip                                          useragent blacklisted
0    bob      login         200  83.149.9.216  Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like M...        True
  userid event_type status_code             ip                                          useragent blacklisted
0   mary      login         200  109.184.11.34  mozilla/5.0 (linux; android 6.0.1; redmi note ...        True
  userid event_type status_code              ip                                          useragent blacklisted
0  james      login         200  198.46.149.143  Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6...        True
    userid event_type status_code          ip                                          useragent blacklisted
0  william      login         200  86.1.76.62  Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) ...        True
   userid event_type status_code              ip                                          useragent blacklisted
0  joseph      login         200  90.220.199.149  Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like M...        True
   userid event_type status_code            ip                                          useragent blacklisted
0  lauren      login         401  71.207.12.53  Mozilla/4.0 (compatible; MSIE 6.0; Windows NT ...        True
   userid event_type status_code            ip                                          useragent blacklisted
0  lauren      login         401  71.207.12.53  Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKi...        True
   userid event_type status_code            ip                                          useragent blacklisted
0  lauren      login         200  71.207.12.53  Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6...        True
  userid event_type status_code             ip                                          useragent blacklisted
0  jules      login         200  109.184.11.34  mozilla/5.0 (linux; android 6.0.1; redmi note ...        True
  userid event_type status_code            ip useragent blacklisted
0  henry      login         401  61.91.63.122   MoZillA        True
  userid event_type status_code            ip            useragent blacklisted
0  henry      login         401  24.78.152.43  ChromeBrowser Agent        True
  userid event_type status_code             ip useragent blacklisted
0  henry      login         401  93.185.116.46   MoZillA        True
  userid event_type status_code             ip useragent blacklisted
0  henry      login         401  198.27.70.131   MoZillA        True
  userid event_type status_code           ip            useragent blacklisted
0  henry      login         401  92.246.9.59  ChromeBrowser Agent        True
  userid event_type status_code             ip            useragent blacklisted
0  henry      login         401  98.120.100.73  ChromeBrowser Agent        True
```

output:
```shell
Connected to pydev debugger (build 211.7628.24)

2021-07-05 12:02:49,140	DEBUG	[enrich]	109.184.11.34 True <DNSBLResult: 109.184.11.34 [BLACKLISTED] (4/56)>
2021-07-05 12:02:49,153	INFO	[stream]	
  userid event_type status_code             ip                                          useragent blacklisted
0   john      login         200  109.184.11.34  mozilla/5.0 (linux; android 6.0.1; redmi note ...        True
2021-07-05 12:02:59,067	DEBUG	[enrich]	83.149.9.216 True <DNSBLResult: 83.149.9.216 [BLACKLISTED] (6/56)>
2021-07-05 12:02:59,085	INFO	[stream]	
  userid event_type status_code            ip                                          useragent blacklisted
0    bob      login         200  83.149.9.216  Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like M...        True
2021-07-05 12:03:06,387	DEBUG	[enrich]	109.184.11.34 True <DNSBLResult: 109.184.11.34 [BLACKLISTED] (5/56)>
2021-07-05 12:03:06,404	INFO	[stream]	
  userid event_type status_code             ip                                          useragent blacklisted
0   mary      login         200  109.184.11.34  mozilla/5.0 (linux; android 6.0.1; redmi note ...        True
2021-07-05 12:03:16,220	DEBUG	[enrich]	175.45.176.5 False <DNSBLResult: 175.45.176.5  (0/56)>
2021-07-05 12:03:16,238	INFO	[stream]	
    userid event_type status_code            ip                                          useragent blacklisted
0  abigail      login         200  175.45.176.5  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)...       False
2021-07-05 12:03:26,111	DEBUG	[enrich]	218.30.103.62 False <DNSBLResult: 218.30.103.62  (0/56)>
2021-07-05 12:03:26,128	INFO	[stream]	
  userid event_type status_code             ip                                          useragent blacklisted
0   doug      login         200  218.30.103.62  Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKi...       False
2021-07-05 12:03:36,066	DEBUG	[enrich]	198.46.149.143 True <DNSBLResult: 198.46.149.143 [BLACKLISTED] (1/56)>
2021-07-05 12:03:36,084	INFO	[stream]	
  userid event_type status_code              ip                                          useragent blacklisted
0  james      login         200  198.46.149.143  Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6...        True
2021-07-05 12:03:46,153	DEBUG	[enrich]	86.1.76.62 True <DNSBLResult: 86.1.76.62 [BLACKLISTED] (3/56)>
2021-07-05 12:03:46,171	INFO	[stream]	
    userid event_type status_code          ip                                          useragent blacklisted
0  william      login         200  86.1.76.62  Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) ...        True
2021-07-05 12:03:56,321	DEBUG	[enrich]	207.241.237.220 False <DNSBLResult: 207.241.237.220  (0/56)>
2021-07-05 12:03:56,340	INFO	[stream]	
  userid event_type status_code               ip                                          useragent blacklisted
0  sally      login         200  207.241.237.220  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8)...       False
2021-07-05 12:04:01,461	DEBUG	[enrich]	175.45.176.5 False <DNSBLResult: 175.45.176.5  (0/56)>
2021-07-05 12:04:01,481	INFO	[stream]	
    userid event_type status_code            ip                                          useragent blacklisted
0  abigail      login         200  175.45.176.5  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)...       False
2021-07-05 12:04:11,783	DEBUG	[enrich]	97.116.185.190 False <DNSBLResult: 97.116.185.190  (0/56)>
2021-07-05 12:04:11,802	INFO	[stream]	
  userid event_type status_code              ip                                          useragent blacklisted
0  emily      login         200  97.116.185.190  Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like M...       False
2021-07-05 12:04:21,920	DEBUG	[enrich]	90.220.199.149 True <DNSBLResult: 90.220.199.149 [BLACKLISTED] (2/56)>
2021-07-05 12:04:21,938	INFO	[stream]	
   userid event_type status_code              ip                                          useragent blacklisted
0  joseph      login         200  90.220.199.149  Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like M...        True
2021-07-05 12:04:32,166	DEBUG	[enrich]	71.207.12.53 True <DNSBLResult: 71.207.12.53 [BLACKLISTED] (2/56)>
2021-07-05 12:04:32,187	INFO	[stream]	
   userid event_type status_code            ip                                          useragent blacklisted
0  lauren      login         401  71.207.12.53  Mozilla/4.0 (compatible; MSIE 6.0; Windows NT ...        True
2021-07-05 12:04:37,413	DEBUG	[enrich]	71.207.12.53 True <DNSBLResult: 71.207.12.53 [BLACKLISTED] (2/56)>
2021-07-05 12:04:37,428	INFO	[stream]	
   userid event_type status_code            ip                                          useragent blacklisted
0  lauren      login         401  71.207.12.53  Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKi...        True
2021-07-05 12:04:42,809	DEBUG	[enrich]	175.45.176.5 False <DNSBLResult: 175.45.176.5  (0/56)>
2021-07-05 12:04:42,824	INFO	[stream]	
    userid event_type status_code            ip                                          useragent blacklisted
0  abigail      login         200  175.45.176.5  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)...       False
2021-07-05 12:04:51,001	DEBUG	[enrich]	71.207.12.53 True <DNSBLResult: 71.207.12.53 [BLACKLISTED] (2/56)>
2021-07-05 12:04:51,010	INFO	[stream]	
   userid event_type status_code            ip                                          useragent blacklisted
0  lauren      login         200  71.207.12.53  Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6...        True
2021-07-05 12:04:51,030	INFO	[stream]	

        userid event_type  status_code            ip                                          useragent blacklisted
count       15         15           15            15                                                 15          15
unique      11          1            2            10                                                  8           2
top     lauren      login          200  71.207.12.53  Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like M...        True
freq         3         15           13             3                                                  3           9


2021-07-05 12:05:01,859	DEBUG	[enrich]	23.20.152.13 False <DNSBLResult: 23.20.152.13  (0/56)>
2021-07-05 12:05:01,879	INFO	[stream]	
      userid event_type status_code            ip                                          useragent blacklisted
0  charlotte      login         200  23.20.152.13  Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53...       False
2021-07-05 12:05:07,406	DEBUG	[enrich]	109.184.11.34 True <DNSBLResult: 109.184.11.34 [BLACKLISTED] (5/56)>
2021-07-05 12:05:07,425	INFO	[stream]	
  userid event_type status_code             ip                                          useragent blacklisted
0  jules      login         200  109.184.11.34  mozilla/5.0 (linux; android 6.0.1; redmi note ...        True
2021-07-05 12:05:18,343	DEBUG	[enrich]	54.255.13.204 False <DNSBLResult: 54.255.13.204  (0/56)>
2021-07-05 12:05:18,353	INFO	[stream]	
   userid event_type status_code             ip                                          useragent blacklisted
0  daniel      login         200  54.255.13.204  Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53...       False
2021-07-05 12:05:23,543	DEBUG	[enrich]	175.45.176.5 False <DNSBLResult: 175.45.176.5  (0/56)>
2021-07-05 12:05:23,559	INFO	[stream]	
    userid event_type status_code            ip                                          useragent blacklisted
0  abigail      login         200  175.45.176.5  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)...       False
2021-07-05 12:05:34,114	DEBUG	[enrich]	175.13.244.207 False <DNSBLResult: 175.13.244.207  (0/56)>
2021-07-05 12:05:34,130	INFO	[stream]	
  userid event_type status_code              ip            useragent blacklisted
0  henry      login         401  175.13.244.207  ChromeBrowser Agent       False
2021-07-05 12:05:44,715	DEBUG	[enrich]	61.91.63.122 True <DNSBLResult: 61.91.63.122 [BLACKLISTED] (6/56)>
2021-07-05 12:05:44,726	INFO	[stream]	
  userid event_type status_code            ip useragent blacklisted
0  henry      login         401  61.91.63.122   MoZillA        True
2021-07-05 12:05:55,428	DEBUG	[enrich]	24.78.152.43 True <DNSBLResult: 24.78.152.43 [BLACKLISTED] (2/56)>
2021-07-05 12:05:55,437	INFO	[stream]	
  userid event_type status_code            ip            useragent blacklisted
0  henry      login         401  24.78.152.43  ChromeBrowser Agent        True
2021-07-05 12:06:06,337	DEBUG	[enrich]	93.185.116.46 True <DNSBLResult: 93.185.116.46 [BLACKLISTED] (2/56)>
2021-07-05 12:06:06,361	INFO	[stream]	
  userid event_type status_code             ip useragent blacklisted
0  henry      login         401  93.185.116.46   MoZillA        True
2021-07-05 12:06:11,885	DEBUG	[enrich]	175.45.176.5 False <DNSBLResult: 175.45.176.5  (0/56)>
2021-07-05 12:06:11,907	INFO	[stream]	
    userid event_type status_code            ip                                          useragent blacklisted
0  abigail      login         200  175.45.176.5  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)...       False
2021-07-05 12:06:23,001	DEBUG	[enrich]	198.27.70.131 True <DNSBLResult: 198.27.70.131 [BLACKLISTED] (2/56)>
2021-07-05 12:06:23,024	INFO	[stream]	
  userid event_type status_code             ip useragent blacklisted
0  henry      login         401  198.27.70.131   MoZillA        True
2021-07-05 12:06:34,244	DEBUG	[enrich]	92.246.9.59 True <DNSBLResult: 92.246.9.59 [BLACKLISTED] (4/56)>
2021-07-05 12:06:34,266	INFO	[stream]	
  userid event_type status_code           ip            useragent blacklisted
0  henry      login         401  92.246.9.59  ChromeBrowser Agent        True
2021-07-05 12:06:44,160	DEBUG	[enrich]	98.120.100.73 True <DNSBLResult: 98.120.100.73 [BLACKLISTED] (1/56)>
2021-07-05 12:06:44,184	INFO	[stream]	
  userid event_type status_code             ip            useragent blacklisted
0  henry      login         401  98.120.100.73  ChromeBrowser Agent        True
2021-07-05 12:06:54,022	DEBUG	[enrich]	46.166.188.244 False <DNSBLResult: 46.166.188.244  (0/56)>
2021-07-05 12:06:54,038	INFO	[stream]	
  userid event_type status_code              ip useragent blacklisted
0  henry      login         401  46.166.188.244   MoZillA       False
2021-07-05 12:06:59,078	DEBUG	[enrich]	175.45.176.5 False <DNSBLResult: 175.45.176.5  (0/56)>
2021-07-05 12:06:59,100	INFO	[stream]	
    userid event_type status_code            ip                                          useragent blacklisted
0  abigail      login         200  175.45.176.5  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)...       False
2021-07-05 12:07:09,133	DEBUG	[enrich]	14.126.79.24 False <DNSBLResult: 14.126.79.24  (0/56)>
2021-07-05 12:07:09,152	INFO	[stream]	
  userid event_type status_code            ip            useragent blacklisted
0  henry      login         401  14.126.79.24  ChromeBrowser Agent       False
2021-07-05 12:07:09,192	INFO	[stream]	

       userid event_type  status_code            ip                                          useragent blacklisted
count      30         30           30            30                                                 30          30
unique     15          1            2            21                                                 11           2
top     henry      login          200  175.45.176.5  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)...        True
freq        9         30           19             6                                                  6          16


2021-07-05 12:07:19,489	DEBUG	[enrich]	218.249.57.178 False <DNSBLResult: 218.249.57.178  (0/56)>
2021-07-05 12:07:19,510	INFO	[stream]	
  userid event_type status_code              ip            useragent blacklisted
0  henry      login         401  218.249.57.178  ChromeBrowser Agent       False
2021-07-05 12:07:29,832	DEBUG	[enrich]	14.189.214.103 True <DNSBLResult: 14.189.214.103 [BLACKLISTED] (4/56)>
2021-07-05 12:07:29,854	INFO	[stream]	
  userid event_type status_code              ip useragent blacklisted
0  henry      login         401  14.189.214.103   MoZillA        True
2021-07-05 12:07:30,095	DEBUG	[enrich]	14.189.214.103 True <DNSBLResult: 14.189.214.103 [BLACKLISTED] (4/56)>
2021-07-05 12:07:30,105	INFO	[stream]	
  userid event_type status_code              ip useragent blacklisted
0  henry      login         401  14.189.214.103   MoZillA        True
2021-07-05 12:07:35,376	DEBUG	[enrich]	175.45.176.5 False <DNSBLResult: 175.45.176.5  (0/56)>
2021-07-05 12:07:35,400	INFO	[stream]	
    userid event_type status_code            ip                                          useragent blacklisted
0  abigail      login         200  175.45.176.5  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)...       False
2021-07-05 12:07:45,966	DEBUG	[enrich]	76.171.199.131 True <DNSBLResult: 76.171.199.131 [BLACKLISTED] (6/56)>
2021-07-05 12:07:45,988	INFO	[stream]	
  userid event_type status_code              ip            useragent blacklisted
0  henry      login         200  76.171.199.131  ChromeBrowser Agent        True
2021-07-05 12:07:51,469	DEBUG	[enrich]	109.184.11.34 True <DNSBLResult: 109.184.11.34 [BLACKLISTED] (5/56)>
2021-07-05 12:07:51,492	INFO	[stream]	
  userid event_type status_code             ip                                          useragent blacklisted
0  roger      login         200  109.184.11.34  mozilla/5.0 (linux; android 6.0.1; redmi note ...        True
2021-07-05 12:07:56,996	DEBUG	[enrich]	175.45.176.5 False <DNSBLResult: 175.45.176.5  (0/56)>
2021-07-05 12:07:57,018	INFO	[stream]	
    userid event_type status_code            ip                                          useragent blacklisted
0  abigail      login         200  175.45.176.5  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)...       False
2021-07-05 12:08:02,556	DEBUG	[enrich]	83.149.9.216 True <DNSBLResult: 83.149.9.216 [BLACKLISTED] (6/56)>
2021-07-05 12:08:02,576	INFO	[stream]	
    userid event_type status_code            ip                                          useragent blacklisted
0  natalia      login         200  83.149.9.216  Mozilla/5.0 (compatible; MSIE 6.0; Windows NT ...        True
2021-07-05 12:08:08,162	DEBUG	[enrich]	175.45.176.5 False <DNSBLResult: 175.45.176.5  (0/56)>
2021-07-05 12:08:08,181	INFO	[stream]	
    userid event_type status_code            ip                                          useragent blacklisted
0  abigail      login         200  175.45.176.5  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)...       False
2021-07-05 12:08:13,864	DEBUG	[enrich]	83.149.9.216 True <DNSBLResult: 83.149.9.216 [BLACKLISTED] (6/56)>
2021-07-05 12:08:13,887	INFO	[stream]	
    userid event_type status_code            ip                                          useragent blacklisted
0  rogrigo      login         200  83.149.9.216  Mozilla/5.0 (Windows; U; Windows NT 5.0) Apple...        True
2021-07-05 12:08:14,132	DEBUG	[enrich]	83.149.9.216 True <DNSBLResult: 83.149.9.216 [BLACKLISTED] (6/56)>
2021-07-05 12:08:14,151	INFO	[stream]	
  userid event_type status_code            ip                                          useragent blacklisted
0   erik      login         200  83.149.9.216  Mozilla/5.0 (Windows; U; Windows NT 5.0) Apple...        True
2021-07-05 12:08:25,539	DEBUG	[enrich]	67.199.248.17 False <DNSBLResult: 67.199.248.17  (0/56)>
2021-07-05 12:08:25,563	INFO	[stream]	
      userid event_type status_code             ip                                          useragent blacklisted
0  christine      login         401  67.199.248.17  Mozilla/5.0 (compatible; MSIE 5.0; Windows NT ...       False
2021-07-05 12:08:25,812	DEBUG	[enrich]	67.199.248.17 False <DNSBLResult: 67.199.248.17  (0/56)>
2021-07-05 12:08:25,831	INFO	[stream]	
      userid event_type status_code             ip                                          useragent blacklisted
0  christine      login         401  67.199.248.17  Mozilla/5.0 (compatible; MSIE 5.0; Windows NT ...       False
2021-07-05 12:08:34,506	DEBUG	[enrich]	67.199.248.17 False <DNSBLResult: 67.199.248.17  (0/56)>
2021-07-05 12:08:34,531	INFO	[stream]	
      userid event_type status_code             ip                                          useragent blacklisted
0  christine      login         200  67.199.248.17  Mozilla/5.0 (compatible; MSIE 5.0; Windows NT ...       False
2021-07-05 12:08:40,391	DEBUG	[enrich]	175.45.176.5 False <DNSBLResult: 175.45.176.5  (0/56)>
2021-07-05 12:08:40,415	INFO	[stream]	
    userid event_type status_code            ip                                          useragent blacklisted
0  abigail      login         200  175.45.176.5  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)...       False
2021-07-05 12:08:40,442	INFO	[stream]	

       userid event_type  status_code            ip                                          useragent blacklisted
count      45         45           45            45                                                 45          45
unique     20          1            2            25                                                 14           2
top     henry      login          200  175.45.176.5  Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)...        True
freq       13         45           29            10                                                 10          23



Process finished with exit code 0
```
