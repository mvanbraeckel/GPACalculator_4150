##
## Makefile to create jar file
##

it :
	@ echo ""
	@ echo "Targets are clean, doc and jar"
	@ echo ""


##
## Create a jar file where the source is in a 'src' subdirectory
##
jar : GPAcalculator.mf
	javac GPAcalculator/*.java
	if [ -d GPAcalculator/src ] ; then rm -rf GPAcalculator/src ; fi
	mkdir GPAcalculator/src
	cp GPAcalculator/*.java GPAcalculator/src
	jar cmf GPAcalculator.mf ../GPAcalculator.jar \
			GPAcalculator/src/*.java GPAcalculator/*.class \
			makefile README.txt
	rm -rf GPAcalculator/src

doc docs :
	if [ -d ../GPAcalculator-classdocs1.1 ] ; then rm -rf ../GPAcalculator-classdocs1.1 ; fi
	mkdir ../GPAcalculator-classdocs1.1
	javadoc -d ../GPAcalculator-classdocs1.1 GPAcalculator/*.java
	( cd ../GPAcalculator-classdocs1.1 ; find . -type d -exec chmod go+rx {} \; ; find . -type f -exec chmod go+r {} \; )

clean : 
	- rm -f GPAcalculator/*.class
	- rm -rf ../GPAcalculator-classdocs1.1
	- rm -rf GPAclaculator/src

