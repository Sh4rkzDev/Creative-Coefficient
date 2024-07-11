# Creative Coefficient

## Technical challenge - Lucas Garcia Campos

### Exercise 1

#### Requirements

* The required fields must be fullfilled (name, last name, email, password, confirm password).
* The *password* and *confirm password* must match.
* The *email* must be a valid address.
* The user must accept the *Terms & cond.* and *Privacy Policy*.
* The user must verify the *reCAPTCHA*.

All of these requirements must be accomplished by the user to be able to register.

#### Assumptions

* The *reCAPTCHA* API is available.

### Exercise 2

Made in branch *feature-ex2*. The pull request is open as requested.

### Exercise 3

Made in branch *feature-ex3* and then merged into *development*.

### Exercise 4

```sql
SELECT page_id FROM pages
LEFT JOIN page_likes 
    ON pages.page_id = page_likes.page_id
WHERE liked_date IS NULL
ORDER BY page_id ASC;
```
