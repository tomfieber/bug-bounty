## Definition of Terms

**Broken Object Level Authorization** 
: Being able to see something you shouldn't be able to see

**Broken Functional Level Authorization** 
: Being able to do something you shouldn't be able to do

**Insecure Direct Object Reference** 
: Kind of an umbrella term

## Checks

- [ ] Understand how the application works
    - How does it fetch/create/modify/delete data?
- [ ] Look for numerical id's in requests
    - URL query string
    - POST body
    - etc.
- [ ] Test with two users and swap ids to see if you can access the other user's data
- [ ] Look for any encrypted/encoded data that may be used to fetch data.
    - Try to understand how it's created and see if we can spoof it
- [ ] Check to see if there is a way to leak the UUID of the other user, if used.
    - Report a user
    - Look at the profile image
    - Any other way of interacting with a user
- [ ] Use a plugin like autorize to help automate testing
- [ ] Can a low user perform admin actions
- [ ] Are boundaries between roles properly enforced?
    - Be sure to check the actual API calls, not just what is in the browser.
- [ ] Check VERBS besides just GET
    - Particularly in state-changing actions

> [!warning] Not every IDOR/BAC constitutes a security vulnerability. If the only thing leaked is information that is already accessible on the site, then it's not a valid vulnerability. Be sure to carefully review the impact for any IDOR/BAC you identify to make sure that it's an actual vulnerability.
