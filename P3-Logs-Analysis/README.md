Project: Logs Analysis  - [Sahil Juneja]
------------------------------------------------
Project Goal: Write server-side code to store a list of your favorite movies, including box art imagery and a movie trailer URL. You will then use your code to generate a static web page allowing visitors to browse their movies and watch the trailers.


Required Libraries and Dependencies
-----------------------------------
This project requires [Udacity's FSND VM](https://github.com/udacity/fullstack-nanodegree-vm).

Follow the instructions to download and set up the Vagrant VM.

- Download and install Virtualbox v5.1 from [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).
- Download and install Vagrant from [here](https://www.vagrantup.com/downloads.html).
- Clone the [FSND VM](https://github.com/udacity/fullstack-nanodegree-vm) repository onto your system.
- Change directory to the `vagrant` directory in the above repo.
- Run `vagrant up` which will download and install the linux OS.
- Run `vagrant ssh` to log into the VM, once installation finishes.

Next,

- Download the data from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
- Unzip the folder, and copy over the `newsdata.sql` file to the `/vagrant/` folder.
- To load the data, from inside your VM - `cd` into the `/vagrant/` directory and use the command `psql -d news -f newsdata.sql`


How to Run Project
------------------
- Follow the instructions linked above to set up the Vagrant VM and download the data.
- Launch Vagrant by running `vagrant up` from within the `vagrant` directory. Then run `vagrant ssh` to log in.
- Navigate to `/vagrant/` inside the VM, and clone or download this project repo.

In the project folder, run the following commands to obtain results to the three questions required for the project:

1. Return top 3 most accessed articles

`python news_log.py --ques 1`

The above will run the `popular_articles()` function. 

2. Return authors with most article views combined

`python news_log.py --ques 2`

The above will run the `popular_authors()` function. 

3. Return days with more than 1% of bad requests

`python news_log.py --ques 3`

The above will run the `error_calc()` function. 

`news_log_outputs.txt` file consists of the output of running all of the above.
