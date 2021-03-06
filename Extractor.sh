# run the shell in the folder where the arcive has to be extracted.
# the script will ask you for the archive.
# zsh: you can make an alias for the script and run it from the shell directly.
read -p "Please enter a file: " var
        if [ -f $var ] ; then
                case $var in
                        *.tar.bz2)      tar xjf $var ;;
                        *.tar.gz)       tar xzf $var ;;
                        *.bz2)          bunzip2 $var ;;
                        *.rar)          unrar x $var ;;
                        *.gz)           gunzip $var ;;
                        *.tar)          tar xf $var ;;
                        *.tbz2)         tar xjf $var ;;
                        *.tgz)          tar xzf $var ;;
                        *.zip)          unzip $var ;;
                        *.Z)            uncompress $var ;;
                        *.7z)           7z x $var ;;
                        *)              echo "'$var' is not a valid file" ;;
                        
                esac
                echo "File succesfully extracted!"
        else
                echo "'$var' is not a valid file"
        fi

