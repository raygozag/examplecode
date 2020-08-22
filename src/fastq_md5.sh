for i in $(ls *${1}*); do
	md5sum ${i}
done > ${2}