import asyncio
import aiohttp
import time
import csv
import aiofiles

usernames = [
    "octocat",
    "sahilsapariya",
    "PRANJALJAVIA",
    "kevintamakuwala"
]

async def fetch_repo_names(username):
    url = f"https://api.github.com/users/{username}/repos"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                repos = await response.json()
                repo_names = [repo['name'] for repo in repos]
                return {
                    "username": username,
                    "repositories": repo_names
                }
            else:
                return {
                    "username": username,
                    "error": response.status,
                    "message": await response.json()
                }
            
async def write_to_csv(data):
    csv_file = 'github_repo.csv'

    async with aiofiles.open(csv_file, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['username', 'repositories'])
        await f.write("username,repositories\n")

        for entry in data:
            repositories_str = "; ".join(entry['repositories'])
            await f.write(f"{entry['username']},{repositories_str}\n")
        

async def main():
    start_time = time.time()
    results = await asyncio.gather(*[fetch_repo_names(username) for username in usernames])

    await write_to_csv(results)

    end_time = time.time()

    print(f"Time taken to complete this task is {(end_time - start_time):.2f} seconds.")


asyncio.run(main())


# OUTPUT:

# github_repo.csv
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# username,repositories
# octocat,boysenberry-repo-1; git-consortium; hello-worId; Hello-World; linguist; octocat.github.io; Spoon-Knife; test-repo1
# sahilsapariya,8086-Programming; Advance-Fastag; All-About-Java; All-about-Python; Blockchain; Blog-Application; Clone-of-UK-government-website; cloud-expense; College360; crack-GRE; e-commerce-product; Elite-Mode; events; Flask-REST-API; hello-world; hostel-management; ML-Basics; movie_app_redux; mytodo; nirmaan-yaatra; Portfolio-sahil; product-visualizer; ranking_system; Role-based-Authentication; sahilsapariya; schoolweb; scrape-up; solar-system
# PRANJALJAVIA,Advance-Fastag; blood_bank_managment_system; Book-Store; Car-Rental-System; College-support_CE045_CE069_CE054_CE049; College360; Community-Website; Doctor_Appointment_Management_System; Expense-Tracker-System; flutter_external_device; GDSC_Task_1; GDSC_Task_2; ggd; myfirstrepo; PRANJALJAVIA; Quiz-Application; Resume-Builder; String_Calculator_TDD_Kata; Study_notes_sharing_website
# kevintamakuwala,Acehacks3.0-WiseNet; AJT-Labwork; Algorithms; App-Dev; ByteBattles; Competitive-Programming; Course-Management; CSES-Solutions; DUHACKS2.0; Duhacks3.0-AnubhavBaatein; FastTyping; FSD-Labwork; J2EE-Todo; Java-Backend; JDBC-CRUD; kevintamakuwala; Lets-Ship-Book-Reviews; LLD-Design-Patterns; Simple-Calculator; StayHomey; University-Permissions

# Time taken to complete this task is 0.80 seconds.
