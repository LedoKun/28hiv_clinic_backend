"""empty message

Revision ID: b58efb8e3aa9
Revises: 
Create Date: 2018-12-02 18:39:26.066988

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b58efb8e3aa9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('icd10',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('icd10WithDescription', sa.Unicode(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('modify_timestamp', sa.DateTime(), nullable=True),
    sa.Column('hn', sa.Unicode(), nullable=True),
    sa.Column('gid', sa.Unicode(), nullable=True),
    sa.Column('cid', sa.Unicode(), nullable=True),
    sa.Column('nap', sa.Unicode(), nullable=True),
    sa.Column('name', sa.Unicode(), nullable=True),
    sa.Column('dob', sa.Date(), nullable=True),
    sa.Column('sex', sa.Unicode(), nullable=True),
    sa.Column('gender', sa.Unicode(), nullable=True),
    sa.Column('marital', sa.Unicode(), nullable=True),
    sa.Column('nationality', sa.Unicode(), nullable=True),
    sa.Column('payer', sa.Unicode(), nullable=True),
    sa.Column('isRefer', sa.Unicode(), nullable=True),
    sa.Column('referFrom', sa.Unicode(), nullable=True),
    sa.Column('education', sa.Unicode(), nullable=True),
    sa.Column('tel', sa.ARRAY(sa.Unicode()), nullable=True),
    sa.Column('relative_tel', sa.ARRAY(sa.Unicode()), nullable=True),
    sa.Column('address', sa.Unicode(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('hn')
    )
    op.create_table('appointment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('modify_timestamp', sa.DateTime(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('appointmentFor', sa.Unicode(), nullable=True),
    sa.Column('patient_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['patient_id'], ['patient.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('investigation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('modify_timestamp', sa.DateTime(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('antiHIV', sa.Unicode(), nullable=True),
    sa.Column('cd4', sa.Integer(), nullable=True),
    sa.Column('pCD4', sa.Integer(), nullable=True),
    sa.Column('vl', sa.Integer(), nullable=True),
    sa.Column('vdrl', sa.Unicode(), nullable=True),
    sa.Column('rpr', sa.Integer(), nullable=True),
    sa.Column('hbsag', sa.Unicode(), nullable=True),
    sa.Column('antiHBs', sa.Unicode(), nullable=True),
    sa.Column('antiHCV', sa.Unicode(), nullable=True),
    sa.Column('ppd', sa.Integer(), nullable=True),
    sa.Column('cxr', sa.Unicode(), nullable=True),
    sa.Column('tb', sa.Unicode(), nullable=True),
    sa.Column('patient_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['patient_id'], ['patient.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('visit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('modify_timestamp', sa.DateTime(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('bw', sa.Float(), nullable=True),
    sa.Column('contactTB', sa.Unicode(), nullable=True),
    sa.Column('adherenceScale', sa.Integer(), nullable=True),
    sa.Column('adherenceProblem', sa.Unicode(), nullable=True),
    sa.Column('delayedDosing', sa.Integer(), nullable=True),
    sa.Column('impression', sa.ARRAY(sa.Unicode()), nullable=True),
    sa.Column('arv', sa.ARRAY(sa.Unicode()), nullable=True),
    sa.Column('oiProphylaxis', sa.ARRAY(sa.Unicode()), nullable=True),
    sa.Column('antiTB', sa.ARRAY(sa.Unicode()), nullable=True),
    sa.Column('vaccination', sa.ARRAY(sa.Unicode()), nullable=True),
    sa.Column('patient_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['patient_id'], ['patient.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('visit')
    op.drop_table('investigation')
    op.drop_table('appointment')
    op.drop_table('patient')
    op.drop_table('icd10')
    # ### end Alembic commands ###
