import pandas as pd
import ast
import re

df = pd.read_csv("list.csv")

results = []
all_ = 0.0
extracted_ = 0.0
#target = open("not_found.txt", "w")
#target_found = open("found.txt", "w")
#target_found.write("{}$${}$${}$${}$${}$${}\n".format("third_party", "url", "regex", "agent", "group", "rest"))
for index, row in df.iterrows():
    all_ += 1
    sentences = row["SENTENCES"][1:-1]
    sentences = sentences.split(">")
    sentences = [s.replace("<Sentence: ", "") for s in sentences[:-1]]
    url = row["URL"]
    third_party = row["ThirdParty"]
    found = False
    
    group = ""
    string = ""
    rest = "" 
    for test_str in sentences:
        regex = r" is [^\.!?(]*(for) "
        matches = re.search(regex, test_str, re.IGNORECASE | re.MULTILINE)
        if matches:
            #print(matches.string)
            #print(matches.group())
            #print(matches.string[matches.span()[1]:])
            #print(matches.string[:matches.span()[0]])
            #print(matches.string[matches.span()[0]:])
            agent = matches.string[:matches.span()[0]]
            rest = matches.string[matches.span()[1]:]
            group = matches.group()
            string = matches.string
            #target_found.write("{}$${}$${}$${}$${}$${}\n".format(third_party, url, regex, agent, group, rest))
            found = True
            break
    
    if not found:
        regex = r"library [^\.!?]*(to|for) "
        for test_str in sentences:
            matches = re.search(regex, test_str, re.IGNORECASE | re.MULTILINE)
            if matches:
                #print(matches.string)
                #print(matches.group())
                #print(matches.string[matches.span()[1]:])
                #print(matches.string[:matches.span()[0]])
                #print(matches.string[matches.span()[0]:])
                agent = matches.string[:matches.span()[0]]
                rest = matches.string[matches.span()[1]:]
                group = matches.group()
                string = matches.string
                #target_found.write("{}$${}$${}$${}$${}$${}\n".format(third_party, url, regex, agent, group, rest))
                found = True
                break
    if not found:
        regex = r"provide[s]? [^\.!?]*(for) "
        for test_str in sentences:
            matches = re.search(regex, test_str, re.IGNORECASE | re.MULTILINE)
            if matches:
                #print(matches.string)
                #print(matches.group())
                #print(matches.string[matches.span()[1]:])
                #print(matches.string[:matches.span()[0]])
                #print(matches.string[matches.span()[0]:])
                agent = matches.string[:matches.span()[0]]
                rest = matches.string[matches.span()[1]:]
                group = matches.group()
                string = matches.string
                #target_found.write("{}$${}$${}$${}$${}$${}\n".format(third_party, url, regex, agent, group, rest))
                found = True
                break
    if not found:
        regex = r"android[s]? [^\.!?]*(library) "
        for test_str in sentences:
            matches = re.search(regex, test_str, re.IGNORECASE | re.MULTILINE)
            if matches:
                #print(matches.string)
                #print(matches.group())
                #print(matches.string[matches.span()[1]:])
                #print(matches.string[:matches.span()[0]])
                #print(matches.string[matches.span()[0]:])
                agent = matches.string[:matches.span()[0]]
                rest = matches.string[matches.span()[1]:]
                group = matches.group()
                string = matches.string
                #target_found.write("{}$${}$${}$${}$${}$${}\n".format(third_party, url, regex, agent, group, rest))
                found = True
                break
    if not found:
        regex = r"way[s]? [^\.!?]*(to) "
        for test_str in sentences:
            matches = re.search(regex, test_str, re.IGNORECASE | re.MULTILINE)
            if matches:
                #print(matches.string)
                #print(matches.group())
                #print(matches.string[matches.span()[1]:])
                #print(matches.string[:matches.span()[0]])
                #print(matches.string[matches.span()[0]:])
                agent = matches.string[:matches.span()[0]]
                rest = matches.string[matches.span()[1]:]
                group = matches.group()
                string = matches.string
                #target_found.write("{}$${}$${}$${}$${}$${}\n".format(third_party, url, regex, agent, group, rest))
                found = True
                break
    if not found:
        regex = r"make[s]? [^\.!?]*(to) "
        for test_str in sentences:
            matches = re.search(regex, test_str, re.IGNORECASE | re.MULTILINE)
            if matches:
                #print(matches.string)
                #print(matches.group())
                #print(matches.string[matches.span()[1]:])
                #print(matches.string[:matches.span()[0]])
                #print(matches.string[matches.span()[0]:])
                agent = matches.string[:matches.span()[0]]
                rest = matches.string[matches.span()[1]:]
                group = matches.group()
                string = matches.string
                #target_found.write("{}$${}$${}$${}$${}$${}\n".format(third_party, url, regex, agent, group, rest))
                found = True
                break
    if not found:
        regex = r"enable[s]? [^\.!?]*(to) "
        for test_str in sentences:
            matches = re.search(regex, test_str, re.IGNORECASE | re.MULTILINE)
            if matches:
                #print(matches.string)
                #print(matches.group())
                #print(matches.string[matches.span()[1]:])
                #print(matches.string[:matches.span()[0]])
                #print(matches.string[matches.span()[0]:])
                agent = matches.string[:matches.span()[0]]
                rest = matches.string[matches.span()[1]:]
                group = matches.group()
                string = matches.string
                #target_found.write("{}$${}$${}$${}$${}$${}\n".format(third_party, url, regex, agent, group, rest))
                found = True
                break
    if not found:
        regex = r"offer[s]? "
        for test_str in sentences:
            matches = re.search(regex, test_str, re.IGNORECASE | re.MULTILINE)
            if matches:
                #print(matches.string)
                #print(matches.group())
                #print(matches.string[matches.span()[1]:])
                #print(matches.string[:matches.span()[0]])
                #print(matches.string[matches.span()[0]:])
                agent = matches.string[:matches.span()[0]]
                rest = matches.string[matches.span()[1]:]
                group = matches.group()
                string = matches.string
                #target_found.write("{}$${}$${}$${}$${}$${}\n".format(third_party, url, regex, agent, group, rest))
                found = True
                break
    if not found:
        regex = r" Android .* library"
        for test_str in sentences:
            matches = re.search(regex, test_str, re.IGNORECASE | re.MULTILINE)
            if matches:
                #print(matches.string)
                #print(matches.group())
                #print(matches.string[matches.span()[1]:])
                #print(matches.string[:matches.span()[0]])
                #print(matches.string[matches.span()[0]:])
                agent = matches.string[:matches.span()[0]]
                rest = matches.string[matches.span()[1]:]
                group = matches.group()
                string = matches.string
                #target_found.write("{}$${}$${}$${}$${}$${}\n".format(third_party, url, regex, agent, group, rest))
                found = True
                break
    if not found:
        regex = r"\bA[n]? .* Android .* to"
        for test_str in sentences:
            matches = re.search(regex, test_str, re.IGNORECASE | re.MULTILINE)
            if matches:
                #print(matches.string)
                #print(matches.group())
                #print(matches.string[matches.span()[1]:])
                #print(matches.string[:matches.span()[0]])
                #print(matches.string[matches.span()[0]:])
                agent = matches.string[:matches.span()[0]]
                rest = matches.string[matches.span()[1]:]
                group = matches.group()
                string = matches.string
                #target_found.write("{}$${}$${}$${}$${}$${}\n".format(third_party, url, regex, agent, group, rest))
                found = True
                break
    if not found:
        regex = r"\bfor .* on Android"
        for test_str in sentences:
            matches = re.search(regex, test_str, re.IGNORECASE | re.MULTILINE)
            if matches:
                #print(matches.string)
                #print(matches.group())
                #print(matches.string[matches.span()[1]:])
                #print(matches.string[:matches.span()[0]])
                #print(matches.string[matches.span()[0]:])
                agent = matches.string[:matches.span()[0]]
                rest = matches.string[matches.span()[1]:]
                group = matches.group()
                string = matches.string
                #target_found.write("{}$${}$${}$${}$${}$${}\n".format(third_party, url, regex, agent, group, rest))
                found = True
                break
    if not found:
        regex = r"\b(A|An|The) .* (library|Android)"
        for test_str in sentences:
            matches = re.search(regex, test_str, re.MULTILINE)
            if matches:
                #print(matches.string)
                #print(matches.group())
                #print(matches.string[matches.span()[1]:])
                #print(matches.string[:matches.span()[0]])
                #print(matches.string[matches.span()[0]:])
                agent = matches.string[:matches.span()[0]]
                rest = matches.string[matches.span()[1]:]
                group = matches.group()
                string = matches.string
                #target_found.write("{}$${}$${}$${}$${}$${}\n".format(third_party, url, regex, agent, group, rest))
                found = True
                break
    if found:
        extracted_ += 1
    """
    if not found:
        for test_str in sentences:
            target.write(test_str)
            target.write("\n")
        target.write("\n\n")
        results.append([row["ThirdParty"], row["URL"], row["SENTENCES"], rest, group, string])
    """
    df2 = pd.DataFrame(results, columns=["ThirdParty", "URL", "SENTENCES", "REST", "GROUP", "STRING"])
    df2.to_csv("out.csv", index=False)
#print(all_, extracted_, extracted_/all_*100.0)