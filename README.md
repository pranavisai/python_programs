Some useful links I have come across while reading:

1. Host, run, and code Python in the cloud -> https://www.pythonanywhere.com/
2. HTTP status codes -> https://httpstatuses.io/
3. Pixela -> https://pixe.la/@pranavisai
4. npoint.io -> For creating personal JSON data API endpoints
5. To create secret key in flask -> python -c "import secrets; print(secrets.token_hex(16))"
6. REST -> REpresentational State Transfer
7. Example of Postman API Documentation -> https://documenter.getpostman.com/view/2568017/TVRhd9qR

## Git Commands
1. "git init" -> To initialize a git repository
2. Staging area -> intermediate stage to see which files to commit to git.
3. "git status" -> to check the status of the repository e.g., like untracked files which are not yet in the staging area.
4. "git add <particular_file_name>" or "git add ." -> to put them in the staging area.
5. "git commit -m "<message_for_commit>"" -> To commit the files and the message to understand what the commit is for.
6. "git log" -> To check the commits made.
7. "git checkout <file_name>" or "git checkout" -> to rollback to previous versions.
8. "git remote add origin <url>" -> to all the remote repository to the local repository.
9. "git push -u origin main" -> push the complete code to the main branch.
10. "git rm --cached -r ." -> to remove all files from the staging area.
11. "git merge <branch-name>" -> to merge the branch with the main branch.
12. https://learngitbranching.js.org/ -> for practicing git commands

## Working with Python Notebook (exploring Pandas DataFrame)
1. df = pd.read_csv('csv_file') -> to read the csv through pandas library.
2. df.head() -> Shows the first 5 rows in the dataframe.
3. df.shape -> To see the number of rows and columns.
4. df.columns -> To access the column names.
5. df.isna() -> To look for NaN (Not A Number) values in the dataframe. NAN values are blank cells or cells that contain strings instead of numbers.
6. df.tail() -> To look at the last rows in the dataframe.
7. c_df = df.dropna() -> To drop the last row and storing into a variable.
8. c_df["column_name] -> For printing all the values of the column.
9. c_df["column_name].max() -> For the max value. 
10. c_df["column_name].idxmax() -> For the index of the max value.
11. c_df["column_name].loc["number of the cell"] or c_df["column_name"]["number of the cell"] -> To get the value in the cell.
12. c_df.loc["number of the cell"] -> To retrieve the complete row with the cell number.
13. c_df["column_name].idxmin(), c_df["column_name].min()-> For the index or value of the min value.
14. c_df["column_name_1] - subtract(["coulmn_name_2"]) -> To find the difference.
15. c_df.insert(column_position, column_name, difference_taken_from_above) -> To insert a column.
16. c_df.sort_values(column_name) -> To sort values in ascending.
17. c_df.sort_values(column_name, ascending=False) -> To sort by descending.
18. c_df.sort_values(by=['col1', 'col2']) -> To sort using multiple columns.
19. c_df.sort_values(by='col1', ascending=False, na_position='first') -> To put NAs first.
20. c_df.groupby('column_name') -> To group by the column name.
21. .count() -> To give the count.
22. .mean() -> To find the average.
23. pd.options.display.float_format = '{:,.2f}'.format -> To round to 2 decimal points.

