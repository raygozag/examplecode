import numpy as np
import pandas as pd
import tensorflow as t
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.utils import to_categorical, plot_model
from sklearn.metrics import confusion_matrix
from keras.layers import Conv2D, MaxPooling2D, Flatten

from eli5.sklearn import PermutationImportance


def permutation_importance(colnames,model,niter,test_data,y_test,random_state):
    sub_data=test_data.to_numpy()
    iloss, iacc = model.evaluate(sub_data, y_test, batch_size=batch_size)
    importances=np.zeros(len(colnames))

    print(test_data.shape)

    for i in range(0, len(colnames)):
        sub_imp=np.zeros(niter)
        for j in range(0,niter):
            sub_pd=test_data.copy(deep=True)
            sub_pd[colnames[i]]=np.random.permutation(sub_pd[colnames[i]])
            sub_pd=sub_pd.to_numpy()
            closs, cacc = model.evaluate(sub_pd, y_test, batch_size=batch_size)
            sub_imp[j]=iacc-cacc
        importances[i]=np.mean(sub_imp)

        importances_pd=pd.DataFrame(list(zip(feature_names,importances)),columns=["feature","weight"])
    return importances_pd



fname="taxa_data_nested_genera.tsv"
train_taxa=pd.read_csv(fname,sep="\t")

len(train_taxa.columns)


exit()
train_taxa

y_train=train_taxa['events'].values

random_state=20
np.random.seed(random_state)
num_labels = len(np.unique(y_train))


set_random_seed(random_state)

num_labels

y_train = to_categorical(y_train)

train_taxa=train_taxa.drop(columns=['events',"X.OTU.ID"])

feature_names=train_taxa.columns

taxa_train_perm=train_taxa.copy(deep=True)

train_taxa=train_taxa.to_numpy()

train_taxa

train_taxa= train_taxa.astype('float32')
input_size=train_taxa.shape[1]

input_size

batch_size = 128
hidden_units = 256
dropout = 0.03




model = Sequential()
model.add(Dense(hidden_units, input_dim=input_size))
model.add(Activation('sigmoid'))
model.add(Dropout(dropout))
model.add(Dense(hidden_units))
model.add(Activation('sigmoid'))
model.add(Dropout(dropout))
model.add(Dense(hidden_units))
model.add(Activation('sigmoid'))
model.add(Dropout(dropout))
model.add(Dense(num_labels))
model.add(Activation('softmax'))
model.summary()

plot_model(model, to_file='mlp-mnist.png', show_shapes=True)

model.compile(loss='categorical_crossentropy',
optimizer='adam',
metrics=['accuracy'])





model.fit(train_taxa, y_train, epochs=100, batch_size=batch_size,class_weight={0:0.1, 1:48})






test_taxa=pd.read_csv(fname,sep="\t")

y_test=to_categorical(test_taxa['events'].values)
y_original=test_taxa['events'].values.astype('int32')

y_original

y_test

test_taxa=test_taxa.drop(columns=['events','X.OTU.ID'])

test_taxa=test_taxa.to_numpy()

test_taxa.shape


loss, acc = model.evaluate(test_taxa, y_test, batch_size=batch_size)

loss
acc

print("\nTest accuracy: %.1f%%" % (100.0 * acc))


y_pred=model.predict_classes(test_taxa).astype('int32')

y_pred

print(confusion_matrix(y_original,y_pred))

random_state=20

#perm = PermutationImportance(model, random_state=random_state,n_iter=15).fit(test_taxa,y_test)
#weights=permutation_importance(feature_names,model,15,taxa_train_perm,y_train,random_state)
#weights=pd.DataFrame(list(zip(feature_names,perm.feature_importances_,perm.feature_importances_std_)),columns=["feature","weight","weight_sd"])

#weights=weights.sort_values(by="weight",ascending=False)

#weights.to_csv("multilpcp_order_taxa_nested_weights.tsv",sep="\t",index=False)