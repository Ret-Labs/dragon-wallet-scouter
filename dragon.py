from Dragon import utils, BundleFinder, ScanAllTx, BulkWalletChecker, CustomBulkWalletCheckerWithConfig, TopTraders, TimestampTransactions, purgeFiles, CopyTradeWalletFinder, TopHolders, checkProxyFile
from Dragon import EthBulkWalletChecker, EthTopTraders, EthTimestampTransactions, EthScanAllTx

purgeFiles = utils.purgeFiles
clear = utils.clear

def eth():
    walletCheck = EthBulkWalletChecker()
    topTraders = EthTopTraders()
    timestamp = EthTimestampTransactions()
    scan = EthScanAllTx()

    filesChoice, files = utils.searchForTxt(chain="Ethereum")
    options, optionsChoice = utils.choices(chain="Ethereum")

    print(f"{optionsChoice}\n")

    while True:
        try:
            while True:
                optionsInput = int(input("[❓] Choice > "))
                if optionsInput in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    print(f"[🐲] Selected {options[optionsInput - 1]}")
                    break 
                else:
                    print("[🐲] Invalid choice.")
            if optionsInput == 1:
                print(f"[🐲] This is a placeholder.")
                print(f"\n{optionsChoice}\n")
            elif optionsInput == 2:
                if len(files) < 2:
                    print("[🐲] No files available.")
                    print(f"\n{optionsChoice}\n")
                    continue
                print(f"\n{filesChoice}\n")

                try:
                    while True:
                        fileSelectionOption = int(input("[❓] File Choice > "))
                        if fileSelectionOption > len(files):
                            print("[🐲] Invalid input.")
                        elif files[fileSelectionOption - 1] == "Select Own File":
                            print(f"[🐲] Selected {files[fileSelectionOption - 1]}")
                            while True:
                                fileDirectory = input("[🐲] Enter filename/path > ")
                                try:
                                    with open(fileDirectory, 'r') as f:
                                        wallets = f.read().splitlines()
                                    if wallets and wallets != []:
                                        print(f"[🐲] Loaded {len(wallets)} wallets") 
                                        break
                                    else:
                                        print(f"[🐲] Error occurred, file may be empty. Go to the ")
                                        continue
                                except Exception as e:
                                    print(f"[🐲] File directory not found.")
                                    continue
                            break
                        else:
                            print(f"[🐲] Selected {files[fileSelectionOption - 1]}")
                            fileDirectory = f"Dragon/data/Ethereum/{files[fileSelectionOption - 1]}"

                            with open(fileDirectory, 'r') as f:
                                wallets = f.read().splitlines()
                            if wallets and wallets != []:
                                print(f"[🐲] Loaded {len(wallets)} wallets")
                                break 
                            else:
                                print(f"[🐲] Error occurred, file may be empty.")
                                continue 
                    while True:
                        threads = input("[❓] Threads > ")
                        try:
                            threads = int(threads)
                            if threads > 100:
                                print(f"[🐲] Do not use more than 100 threads. Automatically set threads to 40.")
                                threads = 40
                        except ValueError:
                            threads = 40
                            print(f"[🐲] Invalid input. Defaulting to 40 threads.")
                            break
                        break
                    while True:
                        skipWallets = False
                        skipWalletsInput = input("[❓] Skip wallets with no buys in 30d (Y/N)> ")

                        if skipWalletsInput.upper() not in ["Y", "N"]:
                            print("[🐲] Invalid input.")
                            continue 
                        if skipWalletsInput.upper() == "N":
                            skipWallets = False
                        else:
                            skipWallets = True
                        walletData = walletCheck.fetchWalletData(wallets, threads=threads, skipWallets=skipWallets)
                        print(f"\n{optionsChoice}\n")
                        break  
                except IndexError as e:
                    print("[🐲] File choice out of range.")
                    print(f"\n{optionsChoice}\n")
                except ValueError:
                    print("[🐲] Invalid input.")
                    print(f"\n{optionsChoice}\n")
                continue
            elif optionsInput == 3:
                while True:
                    threads = input("[❓] Threads > ")
                    try:
                        threads = int(threads)
                        if threads > 100:
                            print(f"[🐲] Do not use more than 100 threads. Automatically set threads to 40.")
                            threads = 40
                    except ValueError:
                        threads = 40
                        print(f"[🐲] Invalid input. Defaulting to 40 threads.")
                    break
                with open('Dragon/data/Ethereum/TopTraders/tokens.txt', 'r') as fp:
                    contractAddresses = fp.read().splitlines()
                    if contractAddresses and contractAddresses != []:
                        print(f"[🐲] Loaded {len(contractAddresses)} contract addresses")
                    else:
                        print(f"[🐲] Error occurred, file may be empty. Go to the file here: Draon/data/Ethereum/tokens.txt")
                        print(f"\n{optionsChoice}\n")
                        continue
                    data = topTraders.topTraderData(contractAddresses, threads)

                print(f"\n{optionsChoice}\n")
            elif optionsInput == 4:
                while True:
                    contractAddress = input("[❓] Contract Address > ")

                    if len(contractAddress) not in [40, 41, 42]:
                        print(f"[🐲] Invalid length.")
                    else:
                        break

                while True:
                    threads = input("[❓] Threads > ")

                    try:
                        threads = int(threads)
                        if threads > 100:
                            print(f"[🐲] Do not use more than 100 threads. Automatically set threads to 40.")
                            threads = 40
                    except ValueError:
                        threads = 40 
                        print(f"[🐲] Invalid input. Defaulting to 40 threads.")
                        break
                    break

                go = scan.getAllTxMakers(contractAddress, threads)
                print(f"\n{optionsChoice}\n")
            elif optionsInput == 5:
                while True:
                    contractAddress = input("[❓] Contract Address > ")

                    if len(contractAddress) not in [40, 41, 42]:
                        print(f"[🐲] Invalid length.")
                    else:
                        break
                while True:
                    threads = input("[❓] Threads > ")
                    try:
                        threads = int(threads)
                        if threads > 100:
                            print(f"[🐲] Do not use more than 100 threads. Automatically set threads to 40.")
                            threads = 40
                    except ValueError:
                        threads = 40 
                        print(f"[🐲] Invalid input. Defaulting to 40 threads.")
                        break
                    break
                print(f"[🐲] Get UNIX Timetstamps Here > https://www.unixtimestamp.com")
                print(f"[🐲] This token was minted at {timestamp.getMintTimestamp(contractAddress)}")
                while True:
                    start = input("[❓] Start UNIX Timestamp > ")
                    try:
                        start = int(start)
                    except ValueError:
                        print(f"[🐲] Invalid input.")
                        break
                    break
                while True:
                    end = input("[❓] End UNIX Timestamp > ")
                    try:
                        start = int(start)
                    except ValueError:
                        print(f"[🐲] Invalid input.")
                        break
                    break
                timestampTxns = timestamp.getTxByTimestamp(contractAddress, threads, start, end)
                print(f"\n{optionsChoice}\n")
            elif optionsInput == 6:
                purgeFiles(chain="Ethereum")
                print(f"[🐲] Successfully purged files.")   
                print(f"\n{optionsChoice}\n")
            elif optionsInput == 7:
                print(f"[🐲] Thank you for using Dragon.")
                break
        except ValueError as e:
            clear()
            print(banner)
            print(f"\n{optionsChoice}\n")
            print("[🐲] Invalid input.")
        except ValueError as e:
            utils.clear()
            print(banner)
            print(f"[🐲] Error occured. Please retry or use a VPN/Proxy. {e}")
            print(f"\n{optionsChoice}\n")
            print("[🐲] Invalid input.")
    

def solana():
    timestamp = TimestampTransactions()
    filesChoice, files = utils.searchForTxt(chain="Solana")
    bundle = BundleFinder()
    scan = ScanAllTx()
    walletCheck = BulkWalletChecker()
    customWalletCheckWithConfig = CustomBulkWalletCheckerWithConfig()
    topTraders = TopTraders()
    copytrade = CopyTradeWalletFinder()
    topHolders = TopHolders()

    options, optionsChoice = utils.choices(chain="Solana")
    print(f"{optionsChoice}\n")
    while True:
        try:
            while True:
                optionsInput = int(input("[❓] Choice > "))
                if optionsInput in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                    print(f"[🐲] Selected {options[optionsInput - 1]}")
                    break 
                else:
                    print("[🐲] Invalid choice.")
        
            if optionsInput == 1:
                if len(files) < 2:
                    print("[🐲] No files available.")
                    continue 

                useProxies = False
                print(f"\n{filesChoice}\n")

                try:
                    while True:
                        fileSelectionOption = int(input("[❓] File Choice > "))
                        if fileSelectionOption > len(files):
                            print("[🐲] Invalid input.")
                        elif files[fileSelectionOption - 1] == "Select Own File":
                            print(f"[🐲] Selected {files[fileSelectionOption - 1]}")
                            while True:
                                fileDirectory = input("[🐲] Enter filename/path > ")
                                try:
                                    with open(fileDirectory, 'r') as f:
                                        wallets = f.read().splitlines()
                                    if wallets and wallets != []:
                                        print(f"[🐲] Loaded {len(wallets)} wallets") 
                                        break
                                    else:
                                        print(f"[🐲] Error occurred, file may be empty. Go to the ")
                                        continue
                                except Exception as e:
                                    print(f"[🐲] File directory not found.")
                                    continue
                            break
                                    
                        else:
                            print(f"[🐲] Selected {files[fileSelectionOption - 1]}")
                            fileDirectory = f"Dragon/data/Solana/{files[fileSelectionOption - 1]}"

                            with open(fileDirectory, 'r') as f:
                                wallets = f.read().splitlines()
                            if wallets and wallets != []:
                                print(f"[🐲] Loaded {len(wallets)} wallets")
                                break 
                            else:
                                print(f"[🐲] Error occurred, file may be empty.")
                                continue 

                    while True:
                        threads = input("[❓] Threads > ")
                        try:
                            threads = int(threads)
                            if threads > 100:
                                print(f"[🐲] Do not use more than 100 threads. Automatically set threads to 40.")
                                threads = 40
                        except ValueError:
                            threads = 40
                            print(f"[🐲] Invalid input. Defaulting to 40 threads.")
                            break
                        break

                    skipWallets = False
                    walletData = customWalletCheckWithConfig.fetchWalletData(wallets, threads=threads, skipWallets=skipWallets, useProxies=useProxies)
                    print(f"\n{optionsChoice}\n")

                except IndexError as e:
                    print("[🐲] File choice out of range.")
                    print(f"\n{optionsChoice}\n")
                except ValueError as e:
                    print(f"[🐲] Invalid input. - {e}")
                    print(f"\n{optionsChoice}\n")
                continue 
            elif optionsInput == 2:
                while True:
                    contractAddress = input("[❓] Contract Address > ")
                    
                    if len(contractAddress) not in [43, 44]:
                        print(f"[🐲] Invalid length.")
                    else:
                        transactionHashes = bundle.teamTrades(contractAddress)
                        bundleData = bundle.checkBundle(transactionHashes[0], transactionHashes[1])
                        formatData = bundle.prettyPrint(bundleData, contractAddress)
                        print(f"\n{formatData}")
                        print(f"\n{optionsChoice}\n")
                        break
            elif optionsInput == 3:
                if len(files) < 2:
                    print("[🐲] No files available.")
                    continue 

                print(f"\n{filesChoice}\n")

                try:
                    while True:
                        fileSelectionOption = int(input("[❓] File Choice > "))
                        if fileSelectionOption > len(files):
                            print("[🐲] Invalid input.")
                        elif files[fileSelectionOption - 1] == "Select Own File":
                            print(f"[🐲] Selected {files[fileSelectionOption - 1]}")
                            while True:
                                fileDirectory = input("[🐲] Enter filename/path > ")
                                try:
                                    with open(fileDirectory, 'r') as f:
                                        wallets = f.read().splitlines()
                                    if wallets and wallets != []:
                                        print(f"[🐲] Loaded {len(wallets)} wallets") 
                                        break
                                    else:
                                        print(f"[🐲] Error occurred, file may be empty. Go to the ")
                                        continue
                                except Exception as e:
                                    print(f"[🐲] File directory not found.")
                                    continue
                            break
                                    
                        else:
                            print(f"[🐲] Selected {files[fileSelectionOption - 1]}")
                            fileDirectory = f"Dragon/data/Solana/{files[fileSelectionOption - 1]}"

                            with open(fileDirectory, 'r') as f:
                                wallets = f.read().splitlines()
                            if wallets and wallets != []:
                                print(f"[🐲] Loaded {len(wallets)} wallets")
                                break 
                            else:
                                print(f"[🐲] Error occurred, file may be empty.")
                                continue 

                    while True:
                        threads = input("[❓] Threads > ")
                        try:
                            threads = int(threads)
                            if threads > 100:
                                print(f"[🐲] Do not use more than 100 threads. Automatically set threads to 40.")
                                threads = 40
                        except ValueError:
                            threads = 40
                            print(f"[🐲] Invalid input. Defaulting to 40 threads.")
                            break
                        break
                    
                    while True:
                        proxies = input("[❓] Use Proxies? (Y/N) > ")
                    
                        try:
                            useProxies = None

                            checkProxies = checkProxyFile()

                            if not checkProxies:
                                print(f"[🐲] Dragon/data/Proxies/proxies.txt is empty, please add proxies to use them.")
                                useProxies = False
                                break

                            if proxies.lower() == "y":
                                useProxies = True
                                print(f"[🐲] Using proxies.")
                            else:
                                useProxies = False
                        except Exception:
                            print(f"[🐲] Invalid input")
                            break
                        break

                    while True:
                        skipWallets = False
                        skipWalletsInput = input("[❓] Skip wallets with no buys in 30d (Y/N) > ")

                        if skipWalletsInput.upper() not in ["Y", "N"]:
                            print("[🐲] Invalid input.")
                            continue 
                        if skipWalletsInput.upper() == "N":
                            skipWallets = False
                        else:
                            skipWallets = True
                        walletData = walletCheck.fetchWalletData(wallets, threads=threads, skipWallets=skipWallets, useProxies=useProxies)
                        print(f"\n{optionsChoice}\n")
                        break  

                except IndexError as e:
                    print("[🐲] File choice out of range.")
                    print(f"\n{optionsChoice}\n")
                except ValueError as e:
                    print(f"[🐲] Invalid input. - {e}")
                    print(f"\n{optionsChoice}\n")
                continue 
            elif optionsInput == 4:
                while True:
                    threads = input("[❓] Threads > ")
                    try:
                        threads = int(threads)
                        if threads > 100:
                            print(f"[🐲] Do not use more than 100 threads. Automatically set threads to 40.")
                            threads = 40
                    except ValueError:
                        threads = 40
                        print(f"[🐲] Invalid input. Defaulting to 40 threads.")
                    break
                
                while True:
                    proxies = input("[❓] Use Proxies? (Y/N) > ")
                
                    try:
                        useProxies = None

                        checkProxies = checkProxyFile()

                        if not checkProxies:
                            print(f"[🐲] Dragon/data/Proxies/proxies.txt is empty, please add proxies to use them.")
                            useProxies = False
                            break

                        if proxies.lower() == "y":
                            useProxies = True
                            print(f"[🐲] Using proxies.")
                        else:
                            useProxies = False
                    except Exception:
                        print(f"[🐲] Invalid input")
                        break
                    break

                with open('Dragon/data/Solana/TopTraders/tokens.txt', 'r') as fp:
                    contractAddresses = fp.read().splitlines()
                    if contractAddresses and contractAddresses != []:
                        print(f"[🐲] Loaded {len(contractAddresses)} contract addresses")
                    else:
                        print(f"[🐲] Error occurred, file may be empty. Go to the file here: Draon/data/TopTraders/tokens.txt")
                        print(f"\n{optionsChoice}\n")
                        continue
                        
                    data = topTraders.topTraderData(contractAddresses, threads, useProxies)

                print(f"\n{optionsChoice}\n")
            elif optionsInput == 5:
                while True:
                    contractAddress = input("[❓] Contract Address > ")

                    if len(contractAddress) not in [43, 44]:
                        print(f"[🐲] Invalid length.")
                    else:
                        break

                while True:
                    threads = input("[❓] Threads > ")

                    try:
                        threads = int(threads)
                        if threads > 100:
                            print(f"[🐲] Do not use more than 100 threads. Automatically set threads to 40.")
                            threads = 40
                    except ValueError:
                        threads = 40 
                        print(f"[🐲] Invalid input. Defaulting to 40 threads.")
                        break
                    break

                while True:
                    proxies = input("[❓] Use Proxies? (Y/N) > ")
                
                    try:
                        useProxies = None

                        checkProxies = checkProxyFile()

                        if not checkProxies:
                            print(f"[🐲] Dragon/data/Proxies/proxies.txt is empty, please add proxies to use them.")
                            useProxies = False
                            break

                        if proxies.lower() == "y":
                            useProxies = True
                            print(f"[🐲] Using proxies.")
                        else:
                            useProxies = False
                    except Exception:
                        print(f"[🐲] Invalid input")
                        break
                    break

                go = scan.getAllTxMakers(contractAddress, threads, useProxies)
                print(f"\n{optionsChoice}\n")

            elif optionsInput == 6:
                while True:
                    contractAddress = input("[❓] Contract Address > ")

                    if len(contractAddress) not in [43, 44]:
                        print(f"[🐲] Invalid length.")
                    else:
                        break
                while True:
                    threads = input("[❓] Threads > ")
                    try:
                        threads = int(threads)
                        if threads > 100:
                            print(f"[🐲] Do not use more than 100 threads. Automatically set threads to 40.")
                            threads = 40
                    except ValueError:
                        threads = 40 
                        print(f"[🐲] Invalid input. Defaulting to 40 threads.")
                        break
                    break
                while True:
                    proxies = input("[❓] Use Proxies? (Y/N) > ")
                
                    try:
                        useProxies = None

                        checkProxies = checkProxyFile()

                        if not checkProxies:
                            print(f"[🐲] Dragon/data/Proxies/proxies.txt is empty, please add proxies to use them.")
                            useProxies = False
                            break

                        if proxies.lower() == "y":
                            useProxies = True
                            print(f"[🐲] Using proxies.")
                        else:
                            useProxies = False
                    except Exception:
                        print(f"[🐲] Invalid input")
                        break
                    break
                print(f"[🐲] Get UNIX Timetstamps Here > https://www.unixtimestamp.com")
                print(f"[🐲] This token was minted at {timestamp.getMintTimestamp(contractAddress, useProxies)}")
                while True:
                    start = input("[❓] Start UNIX Timestamp > ")
                    try:
                        start = int(start)
                    except ValueError:
                        print(f"[🐲] Invalid input.")
                        break
                    break
                while True:
                    end = input("[❓] End UNIX Timestamp > ")
                    try:
                        start = int(start)
                    except ValueError:
                        print(f"[🐲] Invalid input.")
                        break
                    break
                timestampTxns = timestamp.getTxByTimestamp(contractAddress, threads, start, end, useProxies)
                break
            elif optionsInput == 7:
                while True:
                    contractAddress = input("[❓] Contract Address > ")

                    if len(contractAddress) not in [43, 44]:
                        print(f"[🐲] Invalid length.")
                    else:
                        break
                while True:
                    walletAddress = input("[❓] Wallet Address > ")

                    if len(walletAddress) not in [43, 44]:
                        print(f"[🐲] Invalid length.")
                    else:
                        break
                while True:
                    threads = input("[❓] Threads > ")
                    try:
                        threads = int(threads)
                        if threads > 10000:
                            print(f"[🐲] Do not use more than 100 threads. Automatically set threads to 40.")
                            threads = 40
                    except ValueError:
                        threads = 40 
                        print(f"[🐲] Invalid input. Defaulting to 40 threads.")
                        break
                    break
                
                while True:
                    proxies = input("[❓] Use Proxies? (Y/N) > ")
                
                    try:
                        useProxies = None

                        checkProxies = checkProxyFile()

                        if not checkProxies:
                            print(f"[🐲] Dragon/data/Proxies/proxies.txt is empty, please add proxies to use them.")
                            useProxies = False
                            break

                        if proxies.lower() == "y":
                            useProxies = True
                            print(f"[🐲] Using proxies.")
                        else:
                            useProxies = False
                    except Exception:
                        print(f"[🐲] Invalid input")
                        break
                    break

                findWallets = copytrade.findWallets(contractAddress, walletAddress, threads, useProxies)

            elif optionsInput == 8:
                while True:
                    threads = input("[❓] Threads > ")
                    try:
                        threads = int(threads)
                        if threads > 100:
                            print(f"[🐲] Do not use more than 100 threads. Automatically set threads to 40.")
                            threads = 40
                    except ValueError:
                        threads = 40
                        print(f"[🐲] Invalid input. Defaulting to 40 threads.")
                    break
                while True:
                    proxies = input("[❓] Use Proxies? (Y/N) > ")
                
                    try:
                        useProxies = None

                        checkProxies = checkProxyFile()

                        if not checkProxies:
                            print(f"[🐲] Dragon/data/Proxies/proxies.txt is empty, please add proxies to use them.")
                            useProxies = False
                            break

                        if proxies.lower() == "y":
                            useProxies = True
                            print(f"[🐲] Using proxies.")
                        else:
                            useProxies = False
                    except Exception:
                        print(f"[🐲] Invalid input")
                        break
                    break
                with open('Dragon/data/Solana/TopHolders/tokens.txt', 'r') as fp:
                    contractAddresses = fp.read().splitlines()
                    if contractAddresses and contractAddresses != []:
                        print(f"[🐲] Loaded {len(contractAddresses)} contract addresses")
                    else:
                        print(f"[🐲] Error occurred, file may be empty. Go to the file here: Draon/data/TopTraders/tokens.txt")
                        print(f"\n{optionsChoice}\n")
                        continue
                        
                    data = topHolders.topHolderData(contractAddresses, threads, useProxies)

                print(f"\n{optionsChoice}\n")

            elif optionsInput == 9:
                purgeFiles(chain="Solana")
                print(f"[🐲] Successfully purged files.")   
                print(f"\n{optionsChoice}\n")

            elif optionsInput == 10:
                print(f"[🐲] Thank you for using Dragon.")
                break

        except ValueError as e:
            utils.clear()
            print(banner)
            print(f"[🐲] Error occured. Please retry or use a VPN/Proxy. {e}")
            print(f"\n{optionsChoice}\n")
            print("[🐲] Invalid input.")

banner = utils.banner()
print(banner)

chains = utils.chains()[0]
chainsChoice = utils.chains()[1]
print(f"{chainsChoice}\n")

while True:
    try:
        while True:
            chainsInput = int(input("[❓] Choice > "))
            if chainsInput in [1, 2]:
                print(f"[🐲] Selected {chains[chainsInput - 1]}")
                break
            else:
                print("[🐲] Invalid choice.")
        if chainsInput == 1:
            solana()
        elif chainsInput == 2:
            eth()
        else:
            print(f"[🐲] Invalid choice.")
        break
    except ValueError as e:
        utils.clear()
        print(banner)
        print(f"{chainsChoice}\n")
